import re

from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''


class ParsedItem:
    """
    A class to take in an HTML page (or part of it), and find properties of an item in it.
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def find_item_name(self):
        locator = 'article.product_pod h3 a'  # a inside h3 inside article with class of product_pod
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    def find_item_link(self):
        locator = 'article.product_pod h3 a'
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    def find_item_price(self):
        locator = 'article.product_pod p.price_color'
        item_price = self.soup.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))

    def find_item_rating(self):
        locator = 'article.product_pod p.star-rating'
        item_rating_tag = self.soup.select_one(locator)
        classes = item_rating_tag.attrs['class']  # ['star-rating', 'Three']
        rating_classes = [r for r in classes if r != 'star-rating']
        # # Alternatively
        # rating_classes = filter(lambda x: x != 'star-rating', classes)
        return rating_classes[0]


item = ParsedItem(ITEM_HTML)
print(item.find_item_name())
print(item.find_item_link())
print(item.find_item_price())
print(item.find_item_rating())

from flask import Flask, render_template


app = Flask(__name__)
posts = {
    0: {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return 'Hello, world!'


# post_id is going to be replaced by a number specified by the browser request
@app.route('/posts/<int:post_id>')
def post(post_id):
    # return f"Post title: {post['title']}\n\ncontent: {post['content']}"
    post = posts.get(post_id)
    if post:
        return render_template('posts.html', post=posts.get(post_id))
    else:
        return render_template('404.html', message=f'A post with post id {post_id} was not found.')


if __name__ == '__main__':
    app.run(debug=True)


# Comment

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
posts = {
    0: {
        'id': 0,
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


# post_id is going to be replaced by a number specified by the browser request
@app.route('/posts/<int:post_id>')
def post(post_id):
    # return f"Post title: {post['title']}\n\ncontent: {post['content']}"
    post = posts.get(post_id)
    if post:
        return render_template('posts.html', post=posts.get(post_id))
    else:
        return render_template('404.html', message=f'A post with post id {post_id} was not found.')


@app.route('/posts/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}

        return redirect(url_for('post', post_id=post_id))

    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)

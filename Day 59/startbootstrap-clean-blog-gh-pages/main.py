import requests
from flask import Flask, render_template, abort

app = Flask(__name__)

POSTS_URL = "https://api.npoint.io/b08b04a80ea3d505563c"


@app.route('/')
def home():
    all_posts = requests.get(POSTS_URL, timeout=10).json()
    return render_template('index.html', all_posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def post(index):
    all_posts = requests.get(POSTS_URL, timeout=10).json()
    requested_post = next((p for p in all_posts if p["id"] == index), None)
    if requested_post is None:
        abort(404)
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)

# encoding: utf-8
from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'tiｖtle': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('about.html', posts=posts)


@app.route("/about")
def home():
    return render_template('about', title='About')

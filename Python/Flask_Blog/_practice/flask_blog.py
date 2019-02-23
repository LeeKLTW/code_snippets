# encoding: utf-8
from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationFrom, LoginForm

app = Flask(__name__)
# todo why?
app.config['SECRETE_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Kevin Lee',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Kevin Lee',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


def register():
    pass


def login():
    pass


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)

# encoding: utf-8
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# import secrets
# secrets.token_hex(16)
# app.config['SECRETE_KEY'] = '33f0baa056c172061e5b2394b9cb9915'

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


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} successfully.')
        return redirect(url_for('home'))
    else:
        render_template('')

@app.route("/login",methods=['GET','POST'])
def login():
    pass


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)

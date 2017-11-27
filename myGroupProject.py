import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

@app.route('/')
def home():
    #return '<h1>Welcome to James first server. Thanks for checking it out.</h1>'
    return render_template('home-base.html')


@app.route('/members')
def get_user():
    #return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('members.html')


if __name__ == "__main__":
    app.run(debug=True);

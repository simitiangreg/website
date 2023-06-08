from flask import Blueprint
from flask import Flask, render_template

views = Blueprint(__name__, "views")  # Creating a blueprint named 'views'

@views.route("/")
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/cv')
def cv():
    return render_template('cv.html')

@views.route('/blog')
def blog():
    return render_template('blog.html')

from flask import Blueprint
from flask import Flask, render_template

views = Blueprint(__name__, "views")  # Creating a blueprint named 'views'

@views.route("/")
def home():
    return render_template("home.html")

@views.route('/cv')
def cv():
    return render_template('cv.html')

@views.route('/thoughts')
def blog():
    return render_template('blog.html')

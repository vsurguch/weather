
from flask import render_template, url_for
from app import app

@app.route('/')
def index():
    page = render_template("index.html")
    return page

@app.route('/getWeatherByName/<name>')
def weatherByName(name):
    page = render_template("weather_for_city.html", city=name)
    return page


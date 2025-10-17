from routes import app
from flask import render_template


@app.route('/')
@app.route('/index.html')
def index():

    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/login.html')
def login():
    return "Loign page"

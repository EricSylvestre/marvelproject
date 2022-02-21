from app import app
from flask import render_template

@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')
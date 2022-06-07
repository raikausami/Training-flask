from datetime import datetime
from flask import render_template
from Training_flask import app

@app.route('/')
@app.route('/home')

def home():
    return "Hello world"
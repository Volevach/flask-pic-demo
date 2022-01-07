from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from datetime import datetime

import forms

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


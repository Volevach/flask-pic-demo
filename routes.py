from werkzeug.utils import secure_filename
from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request, send_from_directory
from datetime import datetime
from picutil import allowed_file, validate_image

import forms
import os

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        #if file empty
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        #if file not empty and of allowed extension 
        file_ext = os.path.splitext(file.filename)[1] if os.path.splitext(file.filename)[1] != 'jpeg' else 'jpg'
        if file and allowed_file(file_ext):
            # validate that content is valid image file
            if file_ext != validate_image(file.stream):
                return "Invalid image", 400
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           # return redirect(url_for('download_file', name=filename))
    return render_template('uploader.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
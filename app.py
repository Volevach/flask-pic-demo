from flask import Flask

import secrets

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
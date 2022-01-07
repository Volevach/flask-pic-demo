from flask import Flask

import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
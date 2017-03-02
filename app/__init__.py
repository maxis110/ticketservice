from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = 's3cr3t'
db = SQLAlchemy(app)

from app import views, models



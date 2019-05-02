#this is database module - must exist __init__.py file
import os
#pip3 install flask
#pip3 install flask-sqlalchemy
#pip3 install flask-migrate
#pip3 install flask-login
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask( __name__ , template_folder="../html")

print("Template folder: {0:s}".format(app.template_folder))
basedir = os.path.abspath(os.path.dirname(__file__))

login = LoginManager(app)

class Config(object):
    SECRET_KEY = "baricajezakon321$$$"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from database import models


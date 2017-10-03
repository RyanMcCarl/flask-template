#!/usr/env/python3
#

<<<<<<< HEAD
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config


sys.path.insert(0, os.path.abspath(os.getcwd()))
sys.path.insert(0, os.path.abspath(os.pardir))

db = SQLAlchemy()

def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION') or 'development'
    app.config.from_object(config[config_name])
    try:
        app.config.from_envvar('FLASK_APP_SETTINGS')
    except RuntimeError as e:
        pass

    config[config_name].init_app(app)
    return app, config_name

def create_app(config_name='development'):
    app = Flask(__name__)
    bootstrap.init_app(app)
    db.init_app(app)
    app, config_name = configure_app(app)

=======
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
import sys
import os

sys.path.insert(0, os.path.abspath(os.getcwd()))
sys.path.insert(0, os.path.abspath(os.pardir))
sys.path.insert(0, os.path.expanduser('~/Dropbox/dev/ryanserver'))

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
>>>>>>> ef5d7a1bfbc0b8d3b388e2e8ab1230566bd13fe9

    # attach routes and custom error pages here

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .todo import todo as todo_blueprint
    app.register_blueprint(todo_blueprint)

    return app



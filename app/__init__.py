#!/usr/env/python3
#

import os
import sys
from flask import Flask

#sys.path.insert(0, os.path.abspath(os.getcwd()))
#sys.path.insert(0, os.path.abspath(os.pardir))


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION') or 'development'
    from .config import config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    return app


def create_app(config_name='development'):
    app = Flask(__name__)
    app = configure_app(app)

    from app.models import db
    db.init_app(app)


    # attach routes and custom error pages here

    from .main import main# as main_blueprint
    app.register_blueprint(main)#_blueprint)
    from .todo import todo#as todo_blueprint
    app.register_blueprint(todo)#_blueprint)

    return app



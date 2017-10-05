from flask import current_app, Blueprint, render_template
#from current_app import db

main = Blueprint('main', __name__, url_prefix='/', template_folder='../templates')

from . import views
from . import errors



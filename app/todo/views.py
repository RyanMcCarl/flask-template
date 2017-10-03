from datetime import datetime
from flask import render_template, session, redirect, url_for, make_response
from . import todo
import os
from .. import db
<<<<<<< HEAD
import app

def load_todotxt():
    with open(app.config['TODOTXT_FILE_PATH']) as infile:
=======


def load_todotxt():
    with open(os.path.expanduser('~/Dropbox/notes/todo.txt'), mode='r') as infile:
>>>>>>> ef5d7a1bfbc0b8d3b388e2e8ab1230566bd13fe9
        tasks = sorted([task.strip() for task in infile.readlines()])
    return tasks

@todo.route('/todo/index.html', methods=['GET', 'POST'])
@todo.route('/todo', methods=['GET', 'POST'])
def index():
    return render_template('tasklist.html', tasks=load_todotxt())


#!/usr/bin/env python3
import os
from app import create_app, db
#from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

<<<<<<< HEAD
app = create_app(os.getenv('FLASK_CONFIG') or 'development')
=======
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
>>>>>>> ef5d7a1bfbc0b8d3b388e2e8ab1230566bd13fe9
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
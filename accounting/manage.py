""" 
Path    : manage.py.py
Function:
coding  : utf-8
Version : V1.0
Time    : 2023/1/11 22:11
Author  : Walon Cyler
Modified: 
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from models import *

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

from flask_script import Manager
from models_sep import app

manager = Manager(app)


@manager.command
def runserver():
    print("初始化")

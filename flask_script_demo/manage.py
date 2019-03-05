from flask_script import Manager
from flask_script_demo import app
from db_script import DBManager

manager = Manager(app)


@manager.command
def runserver():
    print("服务器运行")


manager.add_command('db', DBManager)


if __name__ == "__main__":
    manager.run()

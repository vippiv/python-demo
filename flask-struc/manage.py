from app import app
from db_operate import db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

# 构建指令
manage = Manager(app)
# 构建数据库迁移操作
migrate = Migrate(app,db)
# 添加数据库迁移指令
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()
from migrate_demo import app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from exts import db
from models import Article


manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.String(100), nullable=False)
    tags = db.Column(db.Text, nullable=False)


if __name__ == '__main__':
    manager.run()

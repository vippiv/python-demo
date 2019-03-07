from exts import db
from datetime import datetime


class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # tags = db.Column(db.Text, nullable=False)
    # now()获取的是服务器获取的第一次运行的时间
    # now则是每次创建模型的时候，都获取当前的时间
    create_time = db.Column(db.DateTime, default=datetime.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('questions'))


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    mobilephone = db.Column(db.String(11), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    question = db.relationship("Question", backref=db.backref('comments', order_by=id.desc()))
    author = db.relationship("User", backref=db.backref('comments'))

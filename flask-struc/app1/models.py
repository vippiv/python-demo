from db_operate import db,DBO
class User(db.Model,DBO):
    userid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(77),nullable=False,unique=True)
    password = db.Column(db.String(77),nullable=False)
    __tablename__ = 'user'
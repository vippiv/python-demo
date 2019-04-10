from exts import db
from datetime import datetime
from werkzeug.security import check_password_hash


# 会员
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    username = db.Column(db.String(50), nullable=False)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), nullable=False)  # 手机号码
    info = db.Column(db.Text)  # 简介
    avatar = db.Column(db.String(100))  # 头像
    add_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(100), unique=True)  # 唯一标识符

    userlogs = db.relationship("Userlog", backref='users')
    comments = db.relationship("Comment", backref='users')
    moviecols = db.relationship("Moviecol", backref='users')

    def __repr__(self):
        return "<User %s>" % self.username


# 会员日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(50))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Userlog %s>' % self.id


# 标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    movies = db.relationship("Movie", backref='tag')

    def __repr__(self):
        return '<Tag %s>' % self.name


# 电影
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    url = db.Column(db.String(100), nullable=False)
    info = db.Column(db.Text, nullable=False)
    logo = db.Column(db.String(100), nullable=False)
    star = db.Column(db.SmallInteger, nullable=False)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    area = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    realse_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    comments = db.relationship("Comment", backref='movie')
    moviecol = db.relationship("Moviecol", backref='movie')

    def __repr__(self):
        return '<Movie %s>' % self.title


# 上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    logo = db.Column(db.String(100), nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Preview %s>' % self.title


# 评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    add_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Preview %s>' % self.id


# 电影收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    add_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Preview %s>' % self.id


# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    url = db.Column(db.String(100), nullable=False, unique=True)
    add_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Auth %s>' % self.name


# 角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    auths = db.Column(db.String(600), nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Role %s>' % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    pwd = db.Column(db.String(100), nullable=False)
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    add_time = db.Column(db.DateTime, default=datetime.utcnow)
    adminlog = db.relationship("Adminlog", backref='admin')
    oplog = db.relationship("Oplog", backref='admin')

    def __repr__(self):
        return "<Admin %s>" % self.username

    # 验证存储的密码和传递过来的密码
    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


# 管理员日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(50))
    addtime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Adminilog %s>' % self.id


# 操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(50))
    reason = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Oplog %s>' % self.id


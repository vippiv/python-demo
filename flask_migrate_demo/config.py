# 配置文件
import os
DEBUG = True
# dialect+driver://username:password@host:port/database # 链接格式
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSRORD = ''
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'migrate_demo'

# 随机字符串，一般用random自动生成
SECRET_KEY = os.urandom(24)
# 当设置session.permanent = True时，下面的参数将决定有效期多久
PERMANENT_SESSION_LIFETIME = 7

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSRORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

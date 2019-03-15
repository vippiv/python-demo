from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ysh7776...@127.0.0.1/infor'
db = SQLAlchemy(app)

class DBO:
    # 定义函数完成构造对象数据初始化
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self,key,value)

    # 定义一个数据添加操作
    @classmethod
    def add(self, *args, **kwargs):
        if len(args)>0 and isinstance(*args, list):
            for dict in args[0]:
                obj = self(**dict)
                db.session.add(obj)
        else:
            obj = self(**kwargs)
            db.session.add(obj)
        db.session.commit()
        return obj

    # 定义函数完成数据更新
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self,key):
                setattr(self, key, value)
        db.session.commit()

    # 定义函数完成数据删除
    def delete(self):
        db.session.delete(self)
        db.session.commit()

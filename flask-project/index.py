from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    db = app.config["DB"]
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS PRODUCT")
    # 使用预处理语句创建表
    sql = """CREATE TABLE PRODUCT (
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
    cursor.execute(sql)
    # 关闭数据库连接
    # db.close()
    return 'Hello'


if __name__ == '__main__':
    app.run()

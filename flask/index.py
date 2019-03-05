from flask import Flask, url_for, render_template, redirect, session, request, g
from utils import login_log
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 定义关系
    author = db.relationship('User', backref=db.backref('articles'))


db.create_all()


@app.route('/')
def index():
    class Child:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    child = Child('ztq', 6)

    context = {
        "username": "zwl",
        "gender": 'male',
        "age": 18,
        'child': child
    }

    return render_template('index.html', **context)


@app.route('/login/')
def login():
    return "login"


@app.route('/u_for')
def u_for():
    print(url_for("hello"))  # url_for 可以根据视图函数反转得到url
    print(url_for("product", ident="10"))
    return 'url for'


@app.route('/filter/')
def hello():
    comments = [
        {
            "user": "之乐他那个",
            "content": "就离开的配偶"
        },
        {
            "user": "跑得快",
            "content": "多念佛感觉到了个"
        }
    ]
    return render_template("filter.html", avatar="http://img2.woyaogexing.com/2019/02/25/0fab280c69cf4d27be816a4545dc1715!400x400.jpeg", comments=comments)


@app.route('/extends/')
def extends_block():
    return render_template("extend_block.html")


@app.route("/articles/")
def article_list():
    # # 增加
    # a1 = Article(title='gg', content='tyjj', author_id=1)
    # db.session.add(a1)
    # # 事务
    # db.session.commit()

    #  查文章
    # a1 = Article.query.filter(Article.title == "aa").first()
    # print("title: %s" % a1.title)
    # print("content: %s" % a1.content)

    # 找文章标题为aa的作者
    # a1 = Article.query.filter(Article.title == "aa").first()
    # print("username:%s" % a1.author.username)

    # 找指定用户的所有文章
    user = User.query.filter(User.username == "li").first()
    result = user.articles
    for article in result:
        print('-'*10)
        print(article.title)

    # # 改
    # a1 = Article.query.filter(Article.title == "aa").first()
    # a1.title = "new title"
    # db.session.commit()

    # # 删
    # a1 = Article.query.filter(Article.content == "bb").first()
    # db.session.delete(a1)
    # db.session.commit()

    article_li = [
        {
            "id": 1,
            "title": "口红成分是什么，用多了对身体有影响吗？",
            "desc": "题主性别女，每次吃饭前长辈都说让我把口红擦了，对身体不好，也为男票身体健康考虑。",
            "date": "2019-8-5"
        },
        {
            "id": 2,
            "title": "有哪些在下班后的闲时稍做点，就有 3000 元月收入的兼职?",
            "desc": "游鱼有水： 去年因故辞职，媳妇一直我养着没让她出去工作，我辞职了她就想在家门口开个小店，我也正好有时间了，就帮她把小店开了起来。调查了好久周边",
            "date": "2019-8-3"
        },
        {
            "id": 3,
            "title": "你考研的时候是怎么查找资料的？",
            "desc": "穆晨王： 昨天在健身房，嗯，洗澡的时候。 我隔壁来了两个姐姐，正对面洗澡，两人都没有拉帘子，就这么坦诚相对着。 他们聊。",
            "date": "2019-8-4"
        }
    ]
    return render_template('article_list.html', articles=article_li)


@app.route('/user/')
def user_list():
    u1 = User(username="li")
    db.session.add(u1)
    db.session.commit()
    return render_template("user.html")


# 动态路由
@app.route("/product/<int:ident>")
def product(ident):
    return "货号： %s" % ident


@app.route("/price/<float:prc>")
def show_price(prc):
    return "price %.2f" % prc


@app.route('/session/')
def session_demo():
    # 如果未指定之间，浏览器回话结束自动删除
    session['username'] = '知乎'
    # 设置下面一句，则过期时间变成31天
    session.permanent = True
    return render_template('session.html')


@app.route('/getsession/')
def get_session():
    # sion = session['username'] # 这个会异常
    sion = session.get('username')
    return render_template('get_session.html', sion = sion)


@app.route("/deletesession/")
def del_session():
    session.pop('username')
    # session.clear() # 删除所有数据
    return 'session删除成功'


@app.route("/from/", methods=["GET", "POST"])
def from_demo():
    print(request.method)
    print(len(request.args))
    if len(request.args) > 0:
        if request.method == "GET":
            login_info = {
                "username": request.args.get("username"),
                "password": request.args.get("password")
            }
        else:
            login_info = {
                "username": request.form.get("username"),
                "password": request.form.get("password")
            }
        return render_template("from.html", **login_info)
    else:
        return render_template("from.html")


@app.route("/g/", methods=["GET", "POST"])
def g_demo():
    # g对象是全局对象（globals）
    if request.method == "GET":
        # username = request.args.get('username')
        g.username = request.args.get('username')
    else:
        # username = request.form.get('username')
        g.username = request.form.get('username')
    login_log()
    return render_template("g.html")


@app.before_request
def my_before():
    # 这里可以去做一下数据查询，如查询用户
    if session.get("username"):
        g.username = session.get('username')
    print("before request")


# 这是上下文钩子函数
@app.context_processor
def my_content_processor():
    return {"username": "111"}


if __name__ == "__main__":
    app.run()

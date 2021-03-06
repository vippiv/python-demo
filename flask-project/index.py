from flask import Flask, render_template, url_for, request, redirect, session
from exts import db
from models import User, Question, Comment
from functools import wraps
from decorators import login_required
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    questions = Question.query.order_by('-create_time').all()
    return render_template("index.html", questions=questions)


@app.route('/q-list/<page>')
def question_list(page):
    page = int(page)
    questions = Question.query.order_by('-create_time').paginate(page=page, per_page=6)
    return render_template("question_list.html", questions=questions)


# 问题详情
@app.route('/q-detail/<id>')
def question_detail(id):
    question_model = Question.query.filter(Question.id == id).first()
    return render_template('question_detail.html', question=question_model)


# 评论
@app.route('/add_comment/', methods=["POST"])
@login_required
def add_comment():
    content = request.form.get("comment")
    question_id = request.form.get("question_id")

    comment = Comment(content=content)
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    comment.author = user
    question = Question.query.filter(Question.id == question_id).first()
    comment.question = question
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('question_detail', id=question_id))


# 登录
@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return "用户名/密码不能为空"
        else:
            user = User.query.filter(User.username == username, User.password == password).first()
            if user:
                session['user_id'] = user.id
                # 31天内可以不需要登录
                session.permanent = True
                return redirect(url_for('index'))
            else:
                return '账号/密码不正确'


# 注册
@app.route('/register/', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        mobilephone = request.form.get("mobilephone")
        username = request.form.get("username")
        password = request.form.get("password")
        repeatpass = request.form.get("repeat_password")

        # 手机验证，已经注册的不用再次注册
        user = User.query.filter(User.mobilephone == mobilephone).first()
        if user:
            return "该手机号码已经注册，请更换手机号"
        else:
            # 密码验证，两次密码是否一致
            if password != repeatpass:
                return "两次密码不一致"
            else:
                user = User(username=username, mobilephone=mobilephone, password=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


# 注销
@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))


# 发布问答
@app.route('/question/', methods=["GET", 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')

        q = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        q.author = user
        db.session.add(q)
        db.session.commit()

        return redirect(url_for("index"))


# 上下文钩子函数
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, url_for, request, redirect, session
from . import home
from models import User
from exts import db


@home.route('/')
def index():
    return render_template('home/index.html')


# 登录
@home.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('home/login.html')
    else:
        username = request.form.get('username')
        pwd = request.form.get('password')
        if not username or not pwd:
            return "请输入账号和密码"
        else:
            user = User.query.filter(User.username == username, User.pwd == pwd).first()
            if user:
                session['user_id'] = user.id
                # 31天内可以不需要登录
                session.permanent = True
                return redirect(url_for('home.index'))
            else:
                return "账号/密码不正确"


# 登录日志
@home.route('/loginlog/')
def loginlog():
    return render_template('home/loginlog.html')


# 注册
@home.route('/register/', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("home/register.html")
    else:
        phone = request.form.get('mobilephone')
        username = request.form.get('username')
        pwd = request.form.get('password')
        repwd = request.form.get('repeat_password')
        if pwd != repwd:
            return "两次密码不相同，请重新输入"
        else:
            # 手机验证，已经注册的不用再次注册
            user = User.query.filter(User.mobilephone == phone).first()
            if user:
                return "该手机号码已经注册，请更换手机号"
            else:
                # 密码验证，两次密码是否一致
                if pwd != repwd:
                    return "两次密码不一致"
                else:
                    user = User(username=username, mobilephone=phone, pwd=pwd)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('home.login'))


# 注销
@home.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('home.login'))


# 会员中心
@home.route('/user/')
def user():
    return render_template('home/user.html')


# 密码操作
@home.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')


# 评论记录
@home.route('/comments/')
def comments():
    return render_template('home/comments.html')


# 电影收藏
@home.route('/moviecol/')
def moviecol():
    return render_template('home/moviecol.html')


# 搜索
@home.route('/search', methods=["GET", "POST"])
def search():
    return render_template('home/search.html')


# 播放界面-电影详情
@home.route('/play/')
def play():
    return render_template('home/play.html')


# 上下文钩子函数，必须有这个，否则前台无法切换登录/注销状态
@home.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}

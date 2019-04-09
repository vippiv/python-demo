from . import admin
from flask import render_template, redirect, url_for, request, session, flash
from models import Admin, Tag
from exts import db
from app.admin.forms import LoginForm, TagForm
from functools import wraps
from datetime import datetime


# 登录限制装饰器
def admin_login_req(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("admin"):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.login'))
    return wrapper


# 首页
@admin.route('/')
@admin_login_req
def index():
    return render_template('admin/index.html')


# 登录
@admin.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(username=data['account']).first()
        if not admin.check_pwd(data['pwd']):
            flash('密码错误！')
            return redirect(url_for('admin.login'))
        else:
            session['admin'] = data["account"]
            return render_template('admin/index.html')
    return render_template("admin/login.html", form=form)


# 退出
@admin.route('/logout/')
@admin_login_req
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin.login'))


# 修改密码
@admin.route('/pwd/')
@admin_login_req
def pwd():
    return render_template("admin/pwd.html")


# 添加标签
@admin.route('/tag/add/', methods=["GET", "POST"])
# @admin_login_req
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag(name=data['name'], addtime=datetime.utcnow())
        db.session.add(tag)
        db.session.commit()
        return redirect(url_for('admin.tag_list'))
    return render_template("admin/tag_add.html", form=form)


# 标签列表
@admin.route('/tag/list/')
@admin_login_req
def tag_list():
    return render_template("admin/tag_list.html")


# 添加电影
@admin.route('/movie_add/')
@admin_login_req
def movie_add():
    return render_template("admin/movie_add.html")


# 电影列表
@admin.route('/movie_list/')
@admin_login_req
def movie_list():
    return render_template("admin/movie_list.html")


# 添加预告
@admin.route('/preview_add/')
@admin_login_req
def preview_add():
    return render_template("admin/preview_edit.html")


# 预告列表
@admin.route('/preview_list/')
@admin_login_req
def preview_list():
    return render_template('admin/preview_list.html')


# 会员列表
@admin.route('/user_list/')
@admin_login_req
def user_list():
    return render_template('admin/user_list.html')


# 查看会员
@admin.route('/user_view/<id>')
@admin_login_req
def user_view(id):
    return render_template('admin/user_view.html')


# 评论列表
@admin.route('/comment_list/')
@admin_login_req
def comment_list():
    return render_template('admin/comment_list.html')


# 收藏列表
@admin.route('/collect_list/')
@admin_login_req
def collect_list():
    return render_template('admin/collect_list.html')


# 删除收藏
@admin.route('/collect_list/')
@admin_login_req
def collect_delete():
    return '删除成功'


# 管理员登录日志列表
@admin.route('/logs_operate_log/')
@admin_login_req
def logs_operate_log():
    return render_template('admin/logs_operate_log.html')


# 管理员登录日志列表
@admin.route('/logs_admin_log/')
@admin_login_req
def logs_admin_log():
    return render_template('admin/logs_admin_log.html')


# 会员登录日志列表
@admin.route('/logs_user_log/')
@admin_login_req
def logs_user_log():
    return render_template('admin/logs_user_log.html')


# 添加权限
@admin.route('/auth_add/')
@admin_login_req
def auth_add():
    return render_template('admin/auth_edit.html')


# 权限编辑
@admin.route('/auth_update/')
@admin_login_req
def auth_update():
    return render_template('admin/auth_edit.html')


# 权限删除
@admin.route('/auth_delete/')
@admin_login_req
def auth_delete():
    return '删除成功'


# 权限列表
@admin.route('/auth_list/')
@admin_login_req
def auth_list():
    return render_template('admin/auth_list.html')


# 添加角色
@admin.route('/role_add/')
@admin_login_req
def role_add():
    return render_template('admin/role_edit.html')


# 角色编辑
@admin.route('/role_update/')
@admin_login_req
def role_update():
    return render_template('admin/role_edit.html')


# 角色删除
@admin.route('/role_delete/')
@admin_login_req
def role_delete():
    return '删除成功'


# 角色列表
@admin.route('/role_list/')
@admin_login_req
def role_list():
    return render_template('admin/role_list.html')


# 添加管理员
@admin.route('/admin_add/')
@admin_login_req
def admin_add():
    return render_template('admin/admin_edit.html')


# 管理员列表
@admin.route('/admin_list/')
@admin_login_req
def admin_list():
    return render_template('admin/admin_list.html')

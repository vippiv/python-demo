from . import admin
from flask import render_template, redirect, url_for


# 首页
@admin.route('/')
def index():
    return render_template("admin/index.html")
    # return redirect(url_for('admin.login'))


# 登录
@admin.route('/login/')
def login():
    return render_template("admin/login.html")


# 退出
@admin.route('/logout/')
def logout():
    return redirect(url_for('admin.login'))


# 修改密码
@admin.route('/pwd/')
def pwd():
    return render_template("admin/pwd.html")


# 添加标签
@admin.route('/tag/add/')
def tag_add():
    return render_template("admin/tag_add.html")


# 标签列表
@admin.route('/tag/list/')
def tag_list():
    return render_template("admin/tag_list.html")


# 添加电影
@admin.route('/movie_add/')
def movie_add():
    return render_template("admin/movie_add.html")


# 电影列表
@admin.route('/movie_list/')
def movie_list():
    return render_template("admin/movie_list.html")


# 添加预告
@admin.route('/preview_add/')
def preview_add():
    return redirect(url_for('admin.login'))


# 预告列表
@admin.route('/preview_list/')
def preview_list():
    return redirect(url_for('admin.login'))


# 会员列表
@admin.route('/user_list/')
def user_list():
    return redirect(url_for('admin.login'))


# 评论列表
@admin.route('/comment_list/')
def comment_list():
    return redirect(url_for('admin.login'))


# 收藏列表
@admin.route('/collect_list/')
def collect_list():
    return redirect(url_for('admin.login'))


# 管理员登录日志列表
@admin.route('/logs_operate_log/')
def logs_operate_log():
    return redirect(url_for('admin.login'))


# 管理员登录日志列表
@admin.route('/logs_admin_log/')
def logs_admin_log():
    return redirect(url_for('admin.login'))


# 会员登录日志列表
@admin.route('/logs_user_log/')
def logs_user_log():
    return redirect(url_for('admin.login'))


# 添加权限
@admin.route('/auth_add/')
def auth_add():
    return redirect(url_for('admin.login'))


# 权限列表
@admin.route('/auth_list/')
def auth_list():
    return redirect(url_for('admin.login'))


# 添加角色
@admin.route('/role_add/')
def role_add():
    return redirect(url_for('admin.login'))


# 角色列表
@admin.route('/role_list/')
def role_list():
    return redirect(url_for('admin.login'))


# 添加管理员
@admin.route('/admin_add/')
def admin_add():
    return redirect(url_for('admin.login'))


# 管理员列表
@admin.route('/admin_list/')
def admin_list():
    return redirect(url_for('admin.login'))

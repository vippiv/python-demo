from . import admin
from flask import render_template, redirect, url_for, request


# 首页
@admin.route('/')
def index():
    return redirect(url_for('admin.login'))


# 登录
@admin.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("admin/login.html")
    else:
        admin_name = request.form.get('username')
        admin_pwd = request.form.get('pwd')
        if not admin_name and not admin_pwd:
            return render_template("admin/index.html")


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
    return render_template("admin/preview_edit.html")


# 预告列表
@admin.route('/preview_list/')
def preview_list():
    return render_template('admin/preview_list.html')


# 会员列表
@admin.route('/user_list/')
def user_list():
    return render_template('admin/user_list.html')


# 查看会员
@admin.route('/user_view/<id>')
def user_view(id):
    return render_template('admin/user_view.html')


# 评论列表
@admin.route('/comment_list/')
def comment_list():
    return render_template('admin/comment_list.html')


# 收藏列表
@admin.route('/collect_list/')
def collect_list():
    return render_template('admin/collect_list.html')


# 删除收藏
@admin.route('/collect_list/')
def collect_delete():
    return '删除成功'


# 管理员登录日志列表
@admin.route('/logs_operate_log/')
def logs_operate_log():
    return render_template('admin/logs_operate_log.html')


# 管理员登录日志列表
@admin.route('/logs_admin_log/')
def logs_admin_log():
    return render_template('admin/logs_admin_log.html')


# 会员登录日志列表
@admin.route('/logs_user_log/')
def logs_user_log():
    return render_template('admin/logs_user_log.html')


# 添加权限
@admin.route('/auth_add/')
def auth_add():
    return render_template('admin/auth_edit.html')


# 权限编辑
@admin.route('/auth_update/')
def auth_update():
    return render_template('admin/auth_edit.html')


# 权限删除
@admin.route('/auth_delete/')
def auth_delete():
    return '删除成功'


# 权限列表
@admin.route('/auth_list/')
def auth_list():
    return render_template('admin/auth_list.html')


# 添加角色
@admin.route('/role_add/')
def role_add():
    return render_template('admin/role_edit.html')


# 角色编辑
@admin.route('/role_update/')
def role_update():
    return render_template('admin/role_edit.html')


# 角色删除
@admin.route('/role_delete/')
def role_delete():
    return '删除成功'


# 角色列表
@admin.route('/role_list/')
def role_list():
    return render_template('admin/role_list.html')


# 添加管理员
@admin.route('/admin_add/')
def admin_add():
    return render_template('admin/admin_edit.html')


# 管理员列表
@admin.route('/admin_list/')
def admin_list():
    return render_template('admin/admin_list.html')

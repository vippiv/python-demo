from . import admin
from app import app
from flask import render_template, redirect, url_for, request, session, flash
from models import Admin, Tag, Movie, Preview, User, Comment, Moviecol, Auth, Role, Oplog, Adminlog, Userlog
from exts import db
from app.admin.forms import LoginForm, TagForm, MovieForm, PreviewForm, AdminForm, AuthForm, RoleForm
from functools import wraps
from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
import os
import uuid  # 生成唯一字符串


# 上下文装饰器
@admin.context_processor
def tpl_extra():
    data = dict(
        online_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    return data


# 登录限制装饰器
def admin_login_req(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("admin"):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.login'))
    return wrapper


# 修改文件名称
def change_filename(filename):
    fileinfo = os.path.splitext(filename)  # 分离包含路径的文件名与包含点号的扩展名
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex + fileinfo[-1])
    return filename


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
            session['admin_id'] = admin.id
            adminlog = Adminlog(
                admin_id=admin.id,
                ip=request.remote_addr
            )
            db.session.add(adminlog)
            db.session.commit()
            return render_template('admin/index.html')
    return render_template("admin/login.html", form=form)


# 退出
@admin.route('/logout/')
@admin_login_req
def logout():
    session.pop('admin', None)
    session.pop('admin_id', None)
    return redirect(url_for('admin.login'))


# 修改密码
@admin.route('/pwd/')
@admin_login_req
def pwd():
    return render_template("admin/pwd.html")


# 添加标签
@admin.route('/tag/add/', methods=["GET", "POST"])
@admin_login_req
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag(name=data['name'], addtime=datetime.utcnow())
        db.session.add(tag)
        db.session.commit()
        flash('添加成功！', 'ok')
        oplog = Oplog(
            admin_id=session['admin_id'],
            ip=request.remote_addr,
            reason="添加标签：%s" % data['name']
        )
        db.session.add(oplog)
        db.session.commit()
        return redirect(url_for('admin.tag_add'))
    return render_template("admin/tag_add.html", form=form)


# 编辑标签
@admin.route('/tag/edit/<id>', methods=["GET", "POST"])
@admin_login_req
def tag_edit(id):
    form = TagForm()
    tag = Tag.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data['name']).count()
        if tag.name != data['name'] and tag_count > 0:
            flash("该标签已经存在", "fail")
            return redirect(url_for('admin.tag_edit'))
        tag.name = data['name']
        db.session.add(tag)
        db.session.commit()
        flash('修改成功！', 'ok')
        return redirect(url_for('admin.tag_edit', id=id))
    return render_template("admin/tag_edit.html", form=form, tag=tag)


# 标签列表
@admin.route('/tag/list/<page>')
@admin_login_req
def tag_list(page):
    page = int(page)
    tags = Tag.query.order_by('-addtime').paginate(page=page, per_page=5)
    return render_template("admin/tag_list.html", tags=tags)


# 删除标签
@admin.route('/tag/del/<id>')
@admin_login_req
def tag_del(id):
    tag = Tag.query.filter_by(id=id).first_or_404()
    db.session.delete(tag)
    db.session.commit()
    flash('删除成功', 'ok')
    oplog = Oplog(
        admin_id=session['admin_id'],
        ip=request.remote_addr,
        reason="删除标签：%s" % tag.name
    )
    db.session.add(oplog)
    db.session.commit()
    return redirect(url_for('admin.tag_list', page=1))


# 添加电影
@admin.route('/movie_add/', methods=["GET", "POST"])
@admin_login_req
def movie_add():
    form = MovieForm()
    if form.validate_on_submit():
        data = form.data
        movie = Movie(
            title=data['movie_name'],
            url=data['movie_url'],
            info=data['movie_desc'],
            star=data['movie_star'],
            logo=data['movie_logo'],
            tag_id=data['movie_id'],
            area=data['movie_address'],
            duration=data['movie_duration'],
            realse_time=data['movie_date']
        )
        db.session.add(movie)
        db.session.commit()
        flash('添加成功！', 'ok')
    return render_template("admin/movie_add.html", form=form)


# 编辑电影
@admin.route('/movie_update/<id>', methods=["GET", "POST"])
@admin_login_req
def movie_update(id):
    form = MovieForm()
    movie = Movie.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        movie.title = data['movie_name']
        movie.url = data['movie_url']
        movie.info = data['movie_desc']
        movie.star = data['movie_star']
        movie.logo = data['movie_logo']
        movie.tag_id = data['movie_id']
        movie.area = data['movie_address']
        movie.duration = data['movie_duration']
        movie.realse_time = data['movie_date']
        flash("修改成功！", 'ok')
        return redirect(url_for('admin.movie_update', id=id))
    return render_template("admin/movie_update.html", form=form, movie=movie)


# 删除电影
@admin.route('/movie_delete/<id>')
@admin_login_req
def movie_delete(id):
    movie = Movie.query.filter_by(id=id).first_or_404()
    db.session.delete(movie)
    db.session.commit()
    flash("删除成功！", "ok")
    return redirect(url_for('admin.movie_list', page=1))


# 电影列表
@admin.route('/movie_list/<page>')
@admin_login_req
def movie_list(page):
    page = int(page)
    movies = Movie.query.order_by('id').paginate(page=page, per_page=5)
    return render_template("admin/movie_list.html", movies=movies)


# 添加预告
@admin.route('/preview_add/', methods=["GET", "POST"])
@admin_login_req
def preview_add():
    form = PreviewForm()
    if form.validate_on_submit():
        data = form.data

        file_logo = secure_filename(form.data['logo'].filename)  # 获取上传文件名字
        file_save_path = app.config['UP_DIR']  # 文件上传保存路径
        if not os.path.exists(file_save_path):
            os.makedirs(file_save_path)  # 如果文件保存路径不存在，则创建一个多级目录
            import stat
            os.chmod(file_save_path, stat.S_IRWXU)  # 授予可读写权限
        logo = change_filename(file_logo)  # 文件重命名
        form.data['logo'].save(file_save_path + logo)  # 保存文件到磁盘中

        preview = Preview(
            title=data['title'],
            logo=logo
        )
        db.session.add(preview)
        db.session.commit()
        flash("添加成功！", "ok")
    return render_template("admin/preview_add.html", form=form)


# 编辑预告
@admin.route("/preview_update/<id>")
@admin_login_req
def preview_update(id):
    form = PreviewForm()
    preview = Preview.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        preview.title = data['title']
        preview.logo = data['logo']
        db.session.add(preview)
        db.session.commit()
    return render_template("admin/preview_update.html", form=form, preview=preview)


# 删除预告
@admin.route("/preview_delete/<id>")
@admin_login_req
def preview_delete(id):
    preview = Preview.query.filter_by(id=id).first_or_404()
    db.session.delete(preview)
    db.session.commit()
    flash("删除成功！", 'ok')
    return redirect(url_for('admin.preview_list', page=1))


# 预告列表
@admin.route('/preview_list/<page>')
@admin_login_req
def preview_list(page):
    page = int(page)
    previews = Preview.query.order_by("id").paginate(page=page, per_page=5)
    return render_template('admin/preview_list.html', previews=previews)


# 会员列表
@admin.route('/user_list/<page>')
@admin_login_req
def user_list(page):
    page = int(page)
    users = User.query.order_by("id").paginate(page=page, per_page=5)
    return render_template('admin/user_list.html', users=users)


# 查看会员
@admin.route('/user_view/<id>')
@admin_login_req
def user_view(id):
    user = User.query.filter_by(id=id).first_or_404()
    return render_template('admin/user_view.html', user=user)


# 删除会员
@admin.route('/user_delete/<id>')
@admin_login_req
def user_delete(id):
    user = User.query.filter_by(id=id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    flash("删除成功", "ok")
    return render_template('admin/user_list.html', page=1)


# 评论列表
@admin.route('/comment_list/<page>')
@admin_login_req
def comment_list(page):
    page = int(page)
    comments = Comment.query.join(Movie).join(User).filter(
        Movie.id == Comment.movie_id,
        User.id == Comment.user_id
    ).order_by("id").paginate(page=page, per_page=5)
    return render_template('admin/comment_list.html', comments=comments)


# 删除评论
@admin.route("/comment_delete/<id>")
@admin_login_req
def comment_delete(id):
    comment = Comment.query.filter_by(id=id).first_or_404()
    db.session.delete(comment)
    db.session.commit()
    flash("删除成功！", "ok")
    return redirect(url_for('admim.comment_list', page=1))


# 收藏列表
@admin.route('/collect_list/<page>')
@admin_login_req
def collect_list(page):
    page = int(page)
    cols = Moviecol.query.join(Movie).join(User).filter(
        Movie.id == Moviecol.movie_id,
        User.id == Moviecol.user_id
    ).order_by('id').paginate(page=page, per_page=5)
    return render_template('admin/collect_list.html', cols=cols)


# 删除收藏
@admin.route('/collect_delete/<id>')
@admin_login_req
def collect_delete(id):
    col = Moviecol.query.filter_by(id=id).first_or_404()
    db.session.delete(col)
    db.session.commit()
    flash('删除成功！', "ok")
    return redirect(url_for('admin.collect_list', page=1))


# 管理员操作日志列表
@admin.route('/logs_operate_log/<page>')
@admin_login_req
def logs_operate_log(page):
    page = int(page)
    oplogs = Oplog.query.join(Admin).order_by('id').paginate(page=page, per_page=5)
    return render_template('admin/logs_operate_log.html', oplogs=oplogs)


# 管理员登录日志列表
@admin.route('/logs_admin_log/<page>')
@admin_login_req
def logs_admin_log(page):
    page = int(page)
    adminlogs = Adminlog.query.join(Admin).filter(Admin.id == Adminlog.admin_id).order_by('id').paginate(page=page, per_page=5)
    return render_template('admin/logs_admin_log.html', adminlogs=adminlogs)


# 会员登录日志列表
@admin.route('/logs_user_log/')
@admin_login_req
def logs_user_log():
    return render_template('admin/logs_user_log.html')


# 添加权限
@admin.route('/auth_add/', methods=["GET", "POST"])
@admin_login_req
def auth_add():
    form = AuthForm()
    if form.validate_on_submit():
        data = form.data
        auth = Auth(name=data['name'], url=data['url'])
        db.session.add(auth)
        db.session.commit()
        flash("添加成功！", "ok")
    return render_template('admin/auth_add.html', form=form)


# 权限编辑
@admin.route('/auth_update/<id>', methods=["GET", "POST"])
@admin_login_req
def auth_update(id):
    form = AuthForm()
    auth = Auth.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        auth.name = data['name']
        auth.url = data['url']
        db.session.add(auth)
        db.session.commit()
        flash("编辑成功！", "ok")
    return render_template('admin/auth_edit.html', form=form, auth=auth)


# 权限删除
@admin.route('/auth_delete/<id>')
@admin_login_req
def auth_delete(id):
    auth = Auth.query.filter_by(id=id).first_or_404()
    db.session.delete(auth)
    db.session.commit()
    flash("删除成功！", "ok")
    return redirect(url_for('admin.auth_list', page=1))


# 权限列表
@admin.route('/auth_list/<page>')
@admin_login_req
def auth_list(page):
    page = int(page)
    auths = Auth.query.order_by("id").paginate(page=page, per_page=10)
    return render_template('admin/auth_list.html', auths=auths)


# 添加角色
@admin.route('/role_add/', methods=["GET", "POST"])
@admin_login_req
def role_add():
    form = RoleForm()
    if form.validate_on_submit():
        data = form.data
        role = Role(
            name=data['name'],
            auths=",".join(map(lambda v: str(v), data['auths']))
        )
        db.session.add(role)
        db.session.commit()
        flash("添加成功!", "ok")
        return redirect(url_for('admin.role_add'))
    return render_template('admin/role_add.html', form=form)


# 角色编辑
@admin.route('/role_update/<id>')
@admin_login_req
def role_update(id):
    form = RoleForm()
    role = Role.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        role.name = data['name']
        role.auths = ",".join(map(lambda v: str(v), data['auths']))
        db.session.add(role)
        db.session.commit()
        flash("修改成功！", "ok")
    return render_template('admin/role_edit.html', form=form, role=role)


# 角色删除
@admin.route('/role_delete/<id>')
@admin_login_req
def role_delete(id):
    role = Role.query.filter_by(id=id).first_or_404()
    db.session.delete(role)
    db.session.commit()
    flash("删除成功！", "ok")
    return redirect(url_for('admin.role_list', page=1))


# 角色列表
@admin.route('/role_list/<page>')
@admin_login_req
def role_list(page):
    page = int(page)
    roles = Role.query.order_by("id").paginate(page=page, per_page=5)
    return render_template('admin/role_list.html', roles=roles)


# 添加管理员
@admin.route('/admin_add/', methods=["GET", "POST"])
@admin_login_req
def admin_add():
    form = AdminForm()
    if form.validate_on_submit():
        data = form.data
        adn = Admin(
            username=data['name'],
            pwd=generate_password_hash(data['pwd'], method='pbkdf2:sha1', salt_length=8),
            role_id=data['role_id']
        )
        db.session.add(adn)
        db.session.commit()
        flash("添加成功！", "ok")
        return redirect(url_for('admin.admin_add'))
    return render_template('admin/admin_add.html', form=form)


# 管理员列表
@admin.route('/admin_list/<page>')
@admin_login_req
def admin_list(page):
    page = int(page)
    admins = Admin.query.join(Role).order_by("id").paginate(page=page, per_page=5)
    return render_template('admin/admin_list.html', admins=admins)

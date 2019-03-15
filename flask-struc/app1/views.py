from flask import render_template, Blueprint, request,url_for
from .models import *
import json
# 创建蓝图
app1 = Blueprint('app1', __name__, template_folder='templates',static_folder='static')

# 渲染函数
@app1.route('/login/',endpoint='login')
def show_login():
    return render_template(
        'login.html',
        url_login = url_for('app1.account_login', _external=True)
    )
@app1.route('/test123456789/',endpoint='t')
def show_test():
    return render_template('test0.html')

# 功能函数
# 定义登录功能
@app1.route('/account_login/',methods=['GET','POST'])
def account_login():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        res = User.query.filter(User.username == username).all()
        object = None
        for item in res:
            object=item
        if object is None:
            msg = {'code': 400, 'infor': '用户民不存在,请注册'}
        else:
            if object.password == password:
                msg = {'code': 200, 'infor': '登陆成功'}
            else:
                msg = {'code': 400, 'infor': '密码错误,请重新输入'}
    else:
        msg = {'code': 400, 'infor': '请求方式不正确'}
    return json.dumps(msg)
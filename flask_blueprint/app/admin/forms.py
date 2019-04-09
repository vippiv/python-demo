from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from models import Admin, Tag


class LoginForm(FlaskForm):
    """ 管理员登录表单 """
    account = StringField(
        label="账号",
        validators=[
            DataRequired('请输入账号!')
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
            # "required": "required"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired('请输入密码!')
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",
            # "required": "required"
        }
    )
    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(username=account).count()
        if admin == 0:
            raise ValidationError('账号不存在')


class TagForm(FlaskForm):
    """标签表单"""
    name = StringField(
        label="标签名",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入标签名",
            "required": 'required'
        }
    )
    submit = SubmitField(
        label="添加",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    def validate_name(self, field):
        name = field.data
        tag = Tag.query.filter_by(name=name).count()
        print("%s", tag)
        if tag > 0:
            raise ValidationError('tag已存在')

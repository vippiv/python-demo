from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError
from models import Admin, Tag, Auth, Role


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
        },
        description="标签"
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
        if tag > 0:
            raise ValidationError('tag已存在')


class MovieForm(FlaskForm):
    """电影表单"""
    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.movie_id.choices = [(v.id, v.name) for v in Tag.query.all()]

    movie_name = StringField(
        label="电影名",
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入电影名称',
            'required': 'required'
        }
    )
    movie_url = FileField(
        label='电影文件',
        validators=[
            DataRequired('请上传电影文件！')
        ],
        description='电影文件',
    )
    movie_desc = TextAreaField(
        label="影片简介",
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入电影简介',
            'required': 'required'
        }
    )
    movie_logo = FileField(
        label='封面',
        validators=[
            DataRequired('请上传封面！')
        ],
        description='封面'
    )
    movie_star = SelectField(
        label='星级',
        validators=[
            DataRequired('请选择星级！')
        ],
        description='星级',
        coerce=int,
        choices=[(1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')],
        render_kw={
            'class': "form-control"
        }
    )
    movie_id = SelectField(
        label='标签',
        validators=[
            DataRequired('请选择标签！')
        ],
        coerce=int,
        choices=None,
        description='标签',
        render_kw={
            'class': "form-control"
        }
    )

    movie_address = StringField(
        label='上映地区',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入影片上映地区',
            'required': 'required'
        }
    )
    movie_duration = StringField(
        label='影片时长',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入影片时长',
            'required': 'required'
        }
    )
    movie_date = StringField(
        label='上映时间',
        validators=[
            DataRequired('请选择上映时间！')
        ],
        description='上映时间',
        render_kw={
            'class': "form-control",
            'placeholder': "请选择上映时间！",
            'id': "input_release_time"  # 由于使用了时间控件，需要指定id
        }
    )
    submit = SubmitField(
        label="添加",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class PreviewForm(FlaskForm):
    title = StringField(
        label="预告标题",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入预告标题",
            "required": "required"
        }
    )
    logo = FileField(
        label="预告封面",
        validators=[
            DataRequired('请上传封面！')
        ],
        description='封面'
    )
    submit = SubmitField(
        label="添加",
        render_kw={
            "class": "btn btn-primary",
        }
    )


class AdminForm(FlaskForm):
    """管理员表单"""
    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)
        self.role_id.choices = [(v.id, v.name) for v in Role.query.all()]

    name = StringField(
        label="管理员名",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入用户名（仅限英文及数字）",
            "required": "required"
        }
    )
    pwd = PasswordField(
        label="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码",
            "required": "required"
        }
    )
    repwd = PasswordField(
        label="再次输入密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请再输入密码",
            "required": "required"
        }
    )
    role_id = SelectField(
        label='角色',
        validators=[
            DataRequired('请选择角色！')
        ],
        description='角色',
        coerce=int,
        choices=None,
        render_kw={
            'class': "form-control"
        }
    )
    submit = SubmitField(
        label="添加",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class AuthForm(FlaskForm):
    name = StringField(
        label='权限名称',
        validators=[
            DataRequired('请输入权限名称！')
        ],
        description='请输入权限名称！',
        render_kw={
            'class': "form-control",
            'placeholder': '权限名称'
        }
    )
    url = StringField(
        label='访问链接',
        validators=[
            DataRequired('请输入访问链接！')
        ],
        description='请输入访问链接！',
        render_kw={
            'class': "form-control",
            'placeholder': '链接地址'
        }
    )
    submit = SubmitField(
        label='提交',
        render_kw={
            'class': "btn btn-primary"
        }
    )


class RoleForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(RoleForm, self).__init__(*args, **kwargs)
        self.auths.choices = [(item.id, item.name) for item in Auth.query.all()]

    name = StringField(
        label='角色名称',
        validators=[
            DataRequired('请输入角色名称！')
        ],
        description='请输入角色名称！',
        render_kw={
            'class': "form-control",
            "placeholder": "角色名称"
        }
    )
    auths = SelectMultipleField(
        label='权限列表',
        description='请选择权限列表！',
        render_kw={
            'class': "form-control",
        },
        coerce=int,
        choices=None
    )
    submit = SubmitField(
        label='提交',
        render_kw={
            'class': "btn btn-primary"
        }
    )

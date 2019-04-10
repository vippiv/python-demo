from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField, SelectField
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

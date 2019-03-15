from . import admin


@admin.route('/')
def index():
    return '<h1>后台</h1>'

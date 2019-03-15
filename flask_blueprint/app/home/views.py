from . import home


@home.route('/')
def index():
    return '<h1>前台</h1>'

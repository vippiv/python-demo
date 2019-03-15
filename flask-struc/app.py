from flask import Flask
# from app1.models import *

app = Flask(__name__,template_folder='static/templates')
app.debug=True

from app1.views import app1
app.register_blueprint(app1, url_prefix='/app1')




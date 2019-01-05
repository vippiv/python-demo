from flask import Flask
import config
app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    return 'index page 3'


@app.route('/hello')
def hello():
    return 'Hello World'


# 动态路由
@app.route("/procuct/<int:ident>")
def product(ident):
    return "product %s" % ident


@app.route("/price/<float:prc>")
def show_price(prc):
    return "price %.2f" % prc


if __name__ == "__main__":
    app.run()

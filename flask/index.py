from flask import Flask, url_for, render_template
import config
app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    context = {
        "username": "zwl",
        "gender": 'male',
        "age": 18
    }
    return render_template('index.html', **context)


@app.route('/u_for')
def u_for():
    print(url_for("hello"))  # url_for 可以根据视图函数反转得到url
    print(url_for("product", ident="10"))
    return 'url for'


@app.route('/hello')
def hello():
    return 'Hello World'


# 动态路由
@app.route("/procuct/<int:ident>")
def product(ident):
    return "货号： %s" % ident


@app.route("/price/<float:prc>")
def show_price(prc):
    return "price %.2f" % prc


if __name__ == "__main__":
    app.run()

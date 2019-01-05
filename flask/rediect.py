from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    login_url = url_for("login")
    return redirect(login_url)
    return "这是首页"


@app.route("/login")
def login():
    return "登录页面"


if __name__ == "__main__":
    app.run(debug=True)

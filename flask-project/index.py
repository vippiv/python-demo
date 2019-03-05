from flask import Flask, render_template, url_for
from exts import db
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template("index.html", name="hetyllo")


if __name__ == '__main__':
    app.run()

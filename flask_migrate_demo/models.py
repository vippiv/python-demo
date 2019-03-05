from migrate_demo import app
from exts import db


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.Text, nullable=False)


@app.route("/inster")
def inster():
    a1 = Article(title='aaa', content="aacontent")
    a2 = Article(title="bbb", content="bbcontent")
    db.session.add(a1)
    db.session.add(a2)
    db.session.commit()
    return 'inster'


@app.route('/select')
def select():
    result = Article.query.filter(Article.title == "aaa").first()
    print("title: %s, content: %s" % (result.title, result.content))

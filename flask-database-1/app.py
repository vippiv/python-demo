from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

article_tag = db.Table('article_tag',
                        db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
                       db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
                       )


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)

    tags = db.relationship("Tag", secondary=article_tag, backref=db.backref("articles"))


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


db.create_all()


@app.route('/')
def hello_world():
    # # 增
    # a1 = Article(title="aaa")
    # a2 = Article(title="bbb")
    #
    # t1 = Tag(name="ttt")
    # t2 = Tag(name="ggg")
    #
    # a1.tags.append(t1)
    # a1.tags.append(t2)
    #
    # a2.tags.append(t1)
    # a2.tags.append(t2)
    #
    # db.session.add(a1)
    # db.session.add(a2)
    #
    # db.session.add(t1)
    # db.session.add(t2)
    # db.session.commit()

    # 查
    a1 = Article.query.filter(Article.title == 'aaa').first()
    ts = a1.tags
    for tag in ts:
        print("tag: %s" % tag.name)

    return 'Hello World!'


if __name__ == '__main__':
    app.run()

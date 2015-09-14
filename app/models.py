from datetime import datetime
from . import db

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(255))
    text = db.Column(db.UnicodeText)
    create_time = db.Column(db.DateTime, default=datetime.now())
    publish_time = db.Column(db.DateTime)

def __repr__(self):
    return '<Article %r>' % self.title

def get_article_all():
    return Article.query.all()

def get_article_by_id(id):
    try:
        return Article.query.filter_by(id=id).one()
    except:
        return None

def create_article(title, text):
    article = Article(title=title, text=text, publish_time=datetime.now())
    db.session.add(article)
    db.session.commit()

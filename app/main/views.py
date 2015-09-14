from flask import request, render_template, redirect, url_for, abort

from . import main
from .. import db
from ..models import *

@main.route('/')
def index():
    content = dict()
    content['title'] = 'Home'
    content['article'] = get_article_all()
    return render_template('index.html', content=content)

@main.route('/article/<id>')
def view(id):
    content = dict()
    content['title'] = 'Article'
    content['article'] = get_article_by_id(id)
    if not content['article']:
        abort(404)
    return render_template('view.html', content=content)

@main.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        if title:
            create_article(title, text)
        return redirect(url_for('.index'))
    content = dict()
    content['title'] = 'Article'
    return render_template('create.html', content=content)

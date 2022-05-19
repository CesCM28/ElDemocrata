from flask import (
    Blueprint, render_template, request
)
from app.db import get_db

bp = Blueprint('eldemocrata', __name__)

@bp.route('/', methods=['GET'])
def index():
    db, c = get_db()
    c.execute(
        'select id,description from category where status = 1'
    )
    categorys = c.fetchall()

    c.execute(
        '''select n.id,n.id_category,n.title
            from news n 
            inner join category c
            on n.id_category = c.id
            where c.status = 1 '''
    )
    news = c.fetchall()

    return render_template('eldemocrata/index.html', categorys=categorys, news=news)

@bp.route('/category/<int:idCategory>', methods=['GET'])
def category_layout(idCategory):
    db, c = get_db()

    c.execute(
        '''select id,id_category,title,link_img
        from news where id_category = %s''', (idCategory,)
    )
    news = c.fetchall()

    c.execute(
        'select id,description from category where status = 1'
    )
    categorys = c.fetchall()

    return render_template('eldemocrata/category.html', categorys=categorys, news=news)

@bp.route('/article/<int:idArticle>', methods=['GET'])
def article_layout(idArticle):
    db, c = get_db()

    c.execute(
        '''select id,id_category,title,link_img
        from news where id_category = %s''', (idArticle,)
    )
    news = c.fetchall()

    c.execute(
        'select id,description from category where status = 1'
    )
    categorys = c.fetchall()

    return render_template('eldemocrata/article.html', categorys=categorys, news=news)
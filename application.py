from sre_constants import CATEGORY
from flask import Flask
from flask import (
    render_template, request, session, flash, redirect, url_for
)
from werkzeug.security import check_password_hash
from DataBase.db import get_db

application = Flask(__name__)
INDEX = 1
CATEGORY = 2
ARTICLE = 3

def getCategorys(c):
    c.execute('select id_category,description,icon from categorys where status = 1')
    return c.fetchall()

def getBanners(c, site):
    c.execute('select id_banner,link from banners where site = %s', (site,))
    return c.fetchall()


@application.route('/', methods=['GET'])
def index():
    search = request.args.get('search')

    if search is None:
        search = ''

    db, c = get_db()

    categorys = getCategorys(c)
    banners = getBanners(c, INDEX)

    c.execute(
        '''
        select n.id_news,n.id_category,n.title,n.link_img,n.paragraph1,c.description,n.created_at
            from news n 
            inner join categorys c
            on n.id_category = c.id_category
            where c.status = 1
            and c.id_category not in (4)
            and (n.title like %s
                or n.paragraph1 like %s
                or n.paragraph2 like %s)
            order by n.id_news desc
            limit 9
            ''', ('%' + search + '%', '%' + search + '%', '%' + search + '%')
    )
    news = c.fetchall()

    c.execute(
        '''
        select n.id_news,n.id_category,n.title,n.link_img,n.paragraph1,c.description
            from news n 
            inner join categorys c
            on n.id_category = c.id_category
            where c.status = 1
            and c.id_category in (4)
            and (n.title like %s
                or n.paragraph1 like %s
                or n.paragraph2 like %s)
            order by n.id_news desc
            limit 3
            ''', ('%' + search + '%', '%' + search + '%', '%' + search + '%')
    )
    opinions = c.fetchall()

    return render_template('eldemocrata/index.html', categorys=categorys, news=news, opinions=opinions, banners=banners)

@application.route('/<int:idCategory>/category', methods=['GET'])
def category_layout(idCategory):
    db, c = get_db()

    categorys = getCategorys(c)
    banners = getBanners(c, CATEGORY)

    c.execute(
        '''select id_news,id_category,title,link_img,paragraph1
        from news where id_category = %s
        order by id_news desc''', (idCategory,)
    )
    news = c.fetchall()

    c.execute('select id_news,title,created_at from news order by id_news desc limit 3')
    snews = c.fetchall()

    c.execute('select id_category,description from categorys where id_category = %s''', (idCategory,))
    category = c.fetchone()

    return render_template('eldemocrata/category.html', categorys=categorys, news=news, category=category, snews=snews, banners=banners)


@application.route('/<int:idArticle>/articulo', methods=['GET'])
def article_layout(idArticle):
    db, c = get_db()

    categorys = getCategorys(c)
    banners = getBanners(c, ARTICLE)

    c.execute(
        '''select id_news,id_category,paragraph1,paragraph2,paragraph3,paragraph4,paragraph5,paragraph6,title,subtitle,link_img,link_video,position_video,created_at
        from news where id_news = %s''', (idArticle,)
    )
    news = c.fetchone()

    c.execute('select id_news,title,created_at from news order by id_news desc limit 5')
    snews = c.fetchall()

    return render_template('eldemocrata/article.html', categorys=categorys, news=news, snews=snews, banners=banners)


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

    
    
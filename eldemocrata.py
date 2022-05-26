from distutils.log import debug
from flask import Flask
import os
from flask import (
    render_template, request
)
from DataBase.db import get_db

app = Flask(__name__)
#application.register_blueprint(bp)

#bp = Blueprint('eldemocrata', __name__)

@app.route('/', methods=['GET'])
def index():
    db, c = get_db()
    c.execute(
        'select id_category,description from category where status = 1'
    )
    categorys = c.fetchall()

    c.execute(
        '''select n.id_news,n.id_category,n.title
            from news n 
            inner join category c
            on n.id_category = c.id_category
            where c.status = 1 '''
    )
    news = c.fetchall()

    return render_template('eldemocrata/index.html', categorys=categorys, news=news)

@app.route('/category/<int:idCategory>', methods=['GET'])
def category_layout(idCategory):
    db, c = get_db()

    c.execute(
        '''select id_news,id_category,title,link_img
        from news where id_category = %s''', (idCategory,)
    )
    news = c.fetchall()

    c.execute(
        'select id_category,description from category where status = 1'
    )
    categorys = c.fetchall()

    c.execute(
        'select id_category,description from category where id_category = %s''', (idCategory,)
    )
    category = c.fetchone()
    print(news)

    return render_template('eldemocrata/category.html', categorys=categorys, news=news, category=category)

@app.route('/article/<int:idArticle>', methods=['GET'])
def article_layout(idArticle):
    db, c = get_db()

    c.execute(
        '''select id_news,id_category,paragraph1,paragraph2,paragraph3,paragraph4,paragraph5,paragraph6,title,link_img
        from news where id_news = %s''', (idArticle,)
    )
    news = c.fetchone()
    print(news)

    c.execute(
        'select id_category,description from category where status = 1'
    )
    categorys = c.fetchall()

    return render_template('eldemocrata/article.html', categorys=categorys, news=news)
    

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    app.run()

    
    
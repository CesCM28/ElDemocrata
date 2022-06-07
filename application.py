from flask import Flask
import functools
from logging import error
import os
from flask import (
    render_template, request, session, flash, redirect, url_for
)
from werkzeug.security import check_password_hash
from DataBase.db import get_db

application = Flask(__name__)
#application.register_blueprint(bp)

#bp = Blueprint('eldemocrata', __name__)

@application.route('/', methods=['GET'])
def index():
    db, c = get_db()
    c.execute(
        'select id_category,description from category where status = 1'
    )
    categorys = c.fetchall()

    c.execute(
        '''
        select n.id_news,n.id_category,n.title,n.link_img,n.paragraph1,c.description
            from news n 
            inner join category c
            on n.id_category = c.id_category
            where c.status = 1
            and c.id_category not in (4)
            order by n.id_news
            limit 9
            '''
    )
    news = c.fetchall()

    c.execute(
        '''
        select n.id_news,n.id_category,n.title,n.link_img,n.paragraph1,c.description
            from news n 
            inner join category c
            on n.id_category = c.id_category
            where c.status = 1
            and c.id_category in (4)
            order by n.id_news
            limit 3
            '''
    )
    opinions = c.fetchall()

    return render_template('eldemocrata/index.html', categorys=categorys, news=news, opinions=opinions)

@application.route('/category/<int:idCategory>', methods=['GET'])
def category_layout(idCategory):
    db, c = get_db()

    c.execute(
        '''select id_news,id_category,title,link_img,paragraph1
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

    return render_template('eldemocrata/category.html', categorys=categorys, news=news, category=category)


@application.route('/article/<int:idArticle>', methods=['GET'])
def article_layout(idArticle):
    db, c = get_db()

    c.execute(
        '''select id_news,id_category,paragraph1,paragraph2,paragraph3,paragraph4,paragraph5,paragraph6,title,link_img
        from news where id_news = %s''', (idArticle,)
    )
    news = c.fetchone()

    c.execute(
        'select id_category,description from category where status = 1'
    )
    categorys = c.fetchall()

    return render_template('eldemocrata/article.html', categorys=categorys, news=news)

#@application.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        username = request.form['username']
#        password = request.form['password']
#        db, c = get_db()
#        error = None
#        c.execute(
#            "SELECT id,username,password FROM dbo.users WHERE username like ?", (username)
#        )
#        user = c.fetchone()

#        if user is None:
#            error = 'Usuario y/o contraseña invalida'
#        elif not check_password_hash(user[2], password):
#            error = 'Usuario y/o contraseña invalida'
            

#        if error is None:
#            session.clear()
#            session['user_id'] = user[0]

#            from .Control import control

#            application.register_blueprint(Control.bp)

#            return redirect(url_for('Control.register'))

#        flash(error)

#    return render_template('Control/login.html')


#@application.before_app_request
#def load_logged_in_user():
#    user_id = session.get('user_id')

#    if user_id is None:
#        g.user = None 
#    else:
#        db, c = get_db()
#        c.execute(
#            "select * from users where id = ?", (user_id)
#        )
#        g.user = c.fetchone()


#def login_required(view):
#    @functools.wraps(view)
#    def wrapped_view(**kwargs):
#        if g.user is None:
#            return redirect(url_for('Control.login'))
        
#        return view(**kwargs)

#    return wrapped_view


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

    
    
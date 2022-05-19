from unicodedata import category
from flask import (
    Blueprint, render_template
)
from app.db import get_db

bp = Blueprint('eldemocrata', __name__)

@bp.route('/')
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
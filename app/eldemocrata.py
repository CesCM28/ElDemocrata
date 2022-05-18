from unicodedata import category
from flask import (
    Blueprint, render_template
)
from db import get_db

bp = Blueprint('eldemocrata', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    db, c = get_db()
    c.execute(
        'select * from category where status = 1 order by order'
    )
    categorys = c.fechall()

    return render_template('eldemocrata/index.html', categorys=categorys)
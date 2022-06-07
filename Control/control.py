from logging import error
from flask import (
    Blueprint, flash, g, render_template, request, url_for, session, redirect
)
from werkzeug.security import check_password_hash, generate_password_hash

from ..DataBase.db import get_db
from ..application import login_required

bp = Blueprint('control', __name__)

@bp.route('/contol')
@login_required
def contol():
    db, c = get_db()
    c.execute(
        'select t.id,t.description,u.username,t.completed,t.created_at from todo t JOIN users u on t.created_by = u.id WHERE created_by = ? order by t.created_by desc', (g.user[0])
    )
    news = c.fetchall()

    return render_template('Control/register.html', news=news)
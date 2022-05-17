from flask import (
    Blueprint, render_template
)

bp = Blueprint('eldemocrata', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('eldemocrata/index.html')
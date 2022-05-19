from dis import Instruction
from flask import flash
import flask
import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions


def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host='127.0.0.1', #current_app.config['DATABASE_HOST'],
            user='root', #current_app.config['DATABASE_USER'],
            password='Platanito1*', #current_app.config['DATABASE_PASSWORD'],
            database='eldemocrata'#current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)

    db.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('base de datos inicializada')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
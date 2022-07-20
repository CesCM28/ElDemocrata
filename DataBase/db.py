import mysql.connector
from flask import g


def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host='dbeldemocrata.cggi3z2t9ytu.us-east-1.rds.amazonaws.com', #current_app.config['DATABASE_HOST'],
            user='admin', #current_app.config['DATABASE_USER'],
            password='UPgnR6LnDYka&VW*2T8pYfFDw', #current_app.config['DATABASE_PASSWORD'],
            database='ElDemocrata'#current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.c

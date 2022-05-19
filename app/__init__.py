from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    from . import eldemocrata

    app.register_blueprint(eldemocrata.bp)

    return app
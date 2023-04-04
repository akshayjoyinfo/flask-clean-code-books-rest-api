from os.path import dirname, join

from dotenv import load_dotenv
from flask import Flask
import os
from src.routes.auth import auth
from src.routes.bookmarks import bookmarks
from src.models.base_model import db
from src.extensions import logging_extension, jwt_security_extension, init_extensions


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(test_config)

    init_extensions(app)
    db.init_app(app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run()

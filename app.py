from os.path import dirname, join

from dotenv import load_dotenv
from flask import Flask
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.models.base_model import db


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(test_config)

    @app.get("/")
    def index():
        return {"message": "Hello World", "status": "Done"}

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

    db.init_app(app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run()

from src.routes.auth import auth
from src.routes.bookmarks import bookmarks


class RouteExtension(object):
    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app: object) -> object:
        app.register_blueprint(auth)
        app.register_blueprint(bookmarks)
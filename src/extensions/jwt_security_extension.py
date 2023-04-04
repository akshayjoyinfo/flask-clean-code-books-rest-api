from flask_jwt_extended import JWTManager


class JwtSecurityExtension:
    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app: object) -> object:
        JWTManager(app)

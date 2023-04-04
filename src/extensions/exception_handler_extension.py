from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_401_UNAUTHORIZED
from flask import jsonify, current_app

class ExceptionHandlerExtension:
    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app: object) -> object:
        @app.errorhandler(HTTP_404_NOT_FOUND)
        def handle_404(e):
            current_app.logger.error('Resource not found 404', extra={
                'exception': e
            })
            return jsonify({
                'error': 'Resource not found',
                'status_code': HTTP_404_NOT_FOUND
            }), HTTP_404_NOT_FOUND

        @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
        def handle_500(e):
            current_app.logger.error('Internal Server Error occurred', extra={
                'exception': e
            })
            return jsonify({
                'error': 'Internal Server Error occurred',
                'status_code': HTTP_500_INTERNAL_SERVER_ERROR
            }), HTTP_404_NOT_FOUND

        @app.errorhandler(HTTP_401_UNAUTHORIZED)
        def handle_401(e):
            current_app.logger.error('User is not authorized', extra={
                'exception': e
            })
            return jsonify({
                'error': 'User is not authorized',
                'status_code': HTTP_401_UNAUTHORIZED
            }), HTTP_401_UNAUTHORIZED


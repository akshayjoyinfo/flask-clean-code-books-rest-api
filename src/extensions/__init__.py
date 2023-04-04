from src.extensions.exception_handler_extension import ExceptionHandlerExtension
from src.extensions.jwt_security_extension import JwtSecurityExtension
from src.extensions.logging_extension import Logging
from src.extensions.route_extension import RouteExtension
from src.extensions.swagger_extension import SwaggerExtension


def init_extensions(app):
    logging_extension = Logging(app)
    jwt_security_extension = JwtSecurityExtension(app)
    route_extension = RouteExtension(app)
    exception_handler_extenion = ExceptionHandlerExtension(app)
    swagger_extension = SwaggerExtension(app)

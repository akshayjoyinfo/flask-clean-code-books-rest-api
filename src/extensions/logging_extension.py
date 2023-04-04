from logging.config import dictConfig
import logging
import sys
import json_log_formatter
import json

class Logging(object):
    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app: object) -> object:
        main_logger = logging.getLogger()
        main_logger.setLevel(logging.DEBUG)
        c = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c.setFormatter(formatter)
        json_formatter = json_log_formatter.VerboseJSONFormatter()
        json_handler = logging.FileHandler(filename='/logs/bookmarks/my-log.json')
        json_handler.setFormatter(json_formatter)
        main_logger.addHandler(c)
        main_logger.addHandler(json_handler)

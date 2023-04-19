import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

LOG_TYPE = os.environ.get("LOG_TYPE")  # Default is a Stream handler
LOG_LEVEL = os.environ.get("LOG_LEVEL")

# File Logging Setup
LOG_DIR = os.environ.get("LOG_DIR")
APP_LOG_NAME = os.environ.get("APP_LOG_NAME")
WWW_LOG_NAME = os.environ.get("WWW_LOG_NAME")
LOG_MAX_BYTES = int(os.environ.get("LOG_MAX_BYTES"))
LOG_COPIES = int(os.environ.get("LOG_COPIES"))
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
SWAGGER = {
    'title': "Bookmarks API",
    'uiversion': 3
}
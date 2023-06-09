from app import create_app
import os
import importlib
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from src.models.base_model import db

app = create_app()


MODELS_DIRECTORY = "models"
EXCLUDE_FILES = ["__init__.py"]



def scan_models():
    print('Inside scan_models')
    for dir_path, dir_names, file_names in os.walk(MODELS_DIRECTORY):
        print(dir_path)
        for file_name in file_names:
            if file_name.endswith("py") and file_name not in EXCLUDE_FILES:
                file_path_wo_ext, _ = os.path.splitext((os.path.join(dir_path, file_name)))
                module_name = file_path_wo_ext.replace(os.sep, ".")
                print(module_name)
                importlib.import_module(module_name)


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    scan_models()
    manager.run()

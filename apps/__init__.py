from flask import Flask
import settings
from apps.pollution.view import pol_bp
from exts import db
from apps.file.view import file_bp

def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_object(settings.Config)
    app.register_blueprint(pol_bp)
    
    db.init_app(app)

    return app

def create_fileapp():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_object(settings.File_Config)
    app.register_blueprint(file_bp)
    app.register_blueprint(pol_bp)

    db.init_app(app)
    
    return app
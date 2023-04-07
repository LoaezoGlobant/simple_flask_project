from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
from app import routes, models

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app=app)

    from app.routes import users_bp
    app.register_blueprint(blueprint=users_bp)
    
    return app
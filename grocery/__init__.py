from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from grocery import config
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app=Flask(__name__)
    app.config['FLASK_ENV']= 'development'
    app.config.from_object(config.Config)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
    db.init_app(app)
    login_manager.init_app(app)
    
    
    with app.app_context():
        
        from grocery.routes import views
        from grocery.auth.route import auth
        from grocery.products.routes import products
        
        
        app.register_blueprint(views)
        app.register_blueprint(auth)
        app.register_blueprint(products)
        
        db.create_all()
        migrate.init_app(app, db)
        
        
    return app
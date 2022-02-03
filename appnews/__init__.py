import os.path
from appnews.models import db, User, News, Contoller
from flask import redirect, url_for
from config import Config, ProductionConfig, DevelopmentConfig
from celery import Celery
from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate

celery = Celery(__name__)

def create_app():
    app = Flask(__name__, static_folder="static/")

    if app.config["ENV"] == "development":
        app.config.from_object(DevelopmentConfig)
    elif app.config["ENV"] == "production":
        app.config.from_object(ProductionConfig)

    admin = Admin(app, name="Aggregator", template_mode="bootstrap3", )
    admin.add_view(Contoller(User, db.session,))
    admin.add_view(Contoller(News, db.session))

    login = LoginManager()
    login.init_app(app)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @login.unauthorized_handler
    def unauthorized():
        flash("You must be logged in to view that page.")
        return redirect(url_for("auth.login"))

    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()
        celery.conf.update(app.config)
        register_blueprints(app)

    return app

def register_blueprints(app):
    from appnews.auth.routes import auth
    from appnews.main.routes import main

    app.register_blueprint(auth)
    app.register_blueprint(main)
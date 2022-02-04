from flask import redirect, url_for
from celery import Celery
from flask import Flask,flash
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import ProductionConfig, DevelopmentConfig

migrate = Migrate()
db = SQLAlchemy()
celery = Celery(__name__)
login = LoginManager()
admin = Admin(name="Aggregator", template_mode="bootstrap3")
app = Flask(__name__, static_folder="static/")


def create_app():

    app = Flask(__name__, static_folder="static/")

    if app.config["ENV"] == "development":
        app.config.from_object(DevelopmentConfig)
    elif app.config["ENV"] == "production":
        app.config.from_object(ProductionConfig)


    admin.init_app(app)
    from appnews.models import User, News, Contoller
    admin.add_view(Contoller(User, db.session))
    admin.add_view(Contoller(News, db.session))

    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        celery.conf.update(app.config)
        db.create_all()


    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @login.unauthorized_handler
    def unauthorized():
        flash("You must be logged in to view that page.")
        return redirect(url_for("auth.login"))

    register_blueprints(app)
    return app

def register_blueprints(app):
    from appnews.auth.routes import auth
    from appnews.main.routes import main

    app.register_blueprint(auth)
    app.register_blueprint(main)

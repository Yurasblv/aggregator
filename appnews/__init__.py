import os.path
from appnews.models import db, User, News, Contoller
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from config import Config, ProductionConfig, DevelopmentConfig
from appnews.extension import login, migrate, admin, app, celery


def create_app():
    if app.config["ENV"] == "development":
        app.config.from_object(DevelopmentConfig)
    elif app.config["ENV"] == "production":
        app.config.from_object(ProductionConfig)

    admin.add_view(Contoller(User, db.session))
    admin.add_view(Contoller(News, db.session))

    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()
    celery.conf.update(app.config)

    from appnews.views import auth, main

    app.register_blueprint(auth)
    app.register_blueprint(main)
    return app

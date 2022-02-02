from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin
from flask import Flask
from celery import Celery


celery = Celery(__name__)
app = Flask(__name__, static_folder="static/")
migrate = Migrate()
admin = Admin(app, name="Aggregator", template_mode="bootstrap3",)
login = LoginManager()


@login.user_loader
def load_user(id):
    from appnews.models import User

    return User.query.get(int(id))


@login.unauthorized_handler
def unauthorized():
    flash("You must be logged in to view that page.")
    return redirect(url_for("auth.login"))

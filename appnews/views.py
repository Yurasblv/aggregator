import datetime
from flask import render_template, request, redirect, flash, url_for
from flask import Blueprint
from appnews.forms import RegistrationForm
from appnews.models import db, User, News
from flask_login import logout_user, login_required
from flask_login import current_user, login_user
from appnews.forms import LoginForm
from appnews.tasks import news_parser

auth = Blueprint("auth", __name__)
main = Blueprint("main", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def index():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data, password=form.password.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("main.profile", username=user.username))
        flash("A user already exists with that name ")
    return render_template("index.html", form=form)


@auth.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.profile", username=current_user))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user, remember=True)
            return redirect(
                url_for(
                    "main.profile",
                    username=User.query.filter_by(username=user.username)
                    .first()
                    .username,
                )
            )
        flash("Invalid username/password combination")
    return render_template("login.html", form=form)


@login_required
@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@login_required
@main.route("/profile/<username>")
def profile(username):
    if request.method == "GET":
        return render_template("profile.html")


@login_required
@main.route("/profile/<username>/<category>")
def news_table(username, category):
    try:
        data = News.query.filter_by(category=category).order_by(News.created_at.desc())
        if data:
            current_time = datetime.datetime.now()
            end_time = data.first().created_at + datetime.timedelta(hours=24)
            if (current_time >= end_time) is True:
                news_parser.delay(category)
                data = News.query.filter_by(category=category).order_by(News.created_at.desc())
                return render_template("news.html", data=data)
            return render_template("news.html", data=data)
    except:
        news_parser.delay(category)
        data = News.query.filter_by(category=category).order_by(News.created_at.desc())
        return render_template("news.html", data=data)


from flask import render_template, request, redirect, flash, url_for
from flask import Blueprint
from appnews.models import db, User
from flask_login import logout_user, login_required
from flask_login import current_user, login_user
from appnews.forms import LoginForm, RegistrationForm

auth = Blueprint("auth", __name__)


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

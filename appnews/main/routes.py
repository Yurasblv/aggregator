from flask import Blueprint
import datetime
from flask import render_template, request
from appnews.models import News
from flask_login import login_required

main = Blueprint("main", __name__)


@login_required
@main.route("/profile/<username>")
def profile(username):
    if request.method == "GET":
        return render_template("profile.html")


@login_required
@main.route("/profile/<username>/<category>")
def news_table(username, category):
    from appnews.tasks import news_parser

    try:
        data = News.query.filter_by(category=category).order_by(News.created_at.desc())
        if data:
            current_time = datetime.datetime.now()
            end_time = data.first().created_at + datetime.timedelta(days=7)
            if (current_time >= end_time) is True:
                news_parser.delay(category)
                data = News.query.filter_by(category=category).order_by(
                    News.created_at.desc()
                )
                return render_template("news.html", data=data)
            else:
                return render_template("news.html", data=data)
    except:
        news_parser.delay(category)
        data = News.query.filter_by(category=category).order_by(News.created_at.desc())
        return render_template("news.html", data=data)

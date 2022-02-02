import datetime
from appnews.extension import celery
from appnews import create_app
from appnews.models import News, db
import requests
import json
from celery.schedules import crontab


@celery.task()
def news_parser(category):
    with create_app().app_context():
        return 111111
#         if category == "politics":
#             url = (
#                 'http://api.mediastack.com/v1/news?access_key=e487ad4bb128b050f48e92f37a6e135c&categories=general&languages=en,%20ru&sources=cnn,bbc&keywords=politics'
#             )
#         elif category == "sport":
#             url = (
#                 "http://api.mediastack.com/v1/news?access_key=e487ad4bb128b050f48e92f37a6e135c&categories=sports"
#                 "&languages=en, "
#                 "ru&sources=espn&keywords=sports "
#             )
#         elif category == "finance":
#             url = (
#                 "http://api.mediastack.com/v1/news?access_key=e487ad4bb128b050f48e92f37a6e135c&categories=business"
#                 "&languages=en, "
#                 "ru&sources=abc,time,forbes,guardian"
#             )
#         elif category == "science":
#             url = (
#                 "http://api.mediastack.com/v1/news?access_key=e487ad4bb128b050f48e92f37a6e135c&categories=science"
#                 "&languages=en, "
#                 "ru&sources=abc,time,forbes,guardian,cnn,bbc"
#             )
#         elif category == "health&medicine":
#             url = (
#                 "http://api.mediastack.com/v1/news?access_key=e487ad4bb128b050f48e92f37a6e135c&categories=health"
#                 "&languages=en,ru "
#             )
#         elif category == "weather":
#             url = (
#                 "http://api.mediastack.com/v1/news?access_key=e487ad4bb128b050f48e92f37a6e135c&categories=general"
#                 "&languages=en, "
#                 "ru&sources=bbc,cnn&keywords=weather,climate"
#             )
#         elif category == "music":
#             url = (
#                 "http://api.mediastack.com/v1/news?access_key=e487ad4bb128b050f48e92f37a6e135c&categories=general"
#                 "&languages=en,ru&sources=bbc,cnn&keywords=song&keywords=music "
#             )
#         response = requests.get(url)
#         print(response)
#         if response.status_code == 429:
#             reserve_parser(category)
#         else:
#             json_data = json.loads(response.text).items()
#             for row in json_data:
#                 for item in row:
#                     if isinstance(item, list):
#                         for i in item:
#                             news = News(
#                                 title=i["title"],
#                                 body=i["description"],
#                                 link=i["url"],
#                                 author=i["author"],
#                                 created_at=i["published_at"],
#                                 category=category,
#                             )
#                             if (
#                                 bool(News.query.filter_by(title=news.title).first())
#                                 is False
#                             ):
#                                 db.session.add(news)
#                                 db.session.commit()
#                                 print("Done")
#                             else:
#                                 print("Not Done")
#                                 pass
#
#
# def reserve_parser(category):
#
#     if category == "politics":
#         url = "https://newsapi.org/v2/top-headlines?q=war&politic&government&apiKey=38eb33318900450f8aeb8028cbbcaa18"
#     elif category == "sport":
#         url = "https://newsapi.org/v2/top-headlines?language=en&category=sports&apiKey=38eb33318900450f8aeb8028cbbcaa18"
#     elif category == "finance":
#         url = "https://newsapi.org/v2/top-headlines?language=en&q=business&apiKey=38eb33318900450f8aeb8028cbbcaa18"
#     elif category == "science":
#         url = "https://newsapi.org/v2/top-headlines?language=en&category=science&apiKey=38eb33318900450f8aeb8028cbbcaa18"
#     elif category == "health&medicine":
#         url = "https://newsapi.org/v2/top-headlines?language=en&category=health&apiKey=38eb33318900450f8aeb8028cbbcaa18"
#     elif category == "weather":
#         url = "https://newsapi.org/v2/top-headlines?language=en&category=general&q=weather&apiKey=38eb33318900450f8aeb8028cbbcaa18"
#     elif category == "music":
#         url = "https://newsapi.org/v2/top-headlines?language=en&category=general&q=music&apiKey=38eb33318900450f8aeb8028cbbcaa18"
#     json_data = json.loads(response.text).items()
#     for row in json_data:
#         for item in row:
#             if isinstance(item, list):
#                 for i in item:
#                     news = News(
#                         title=i["title"][:180],
#                         body=i["description"],
#                         link=i["url"],
#                         author=i["author"],
#                         created_at=i["publishedAt"].strip("Z"),
#                         category=category,
#                     )
#                     if bool(News.query.filter_by(title=news.title).first()) is False:
#                         db.session.add(news)
#                         db.session.commit()
#                         print("Done")
#                     else:
#                         print("Not Done")
#                         pass
#
#
# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(
#         crontab(hour=00, minute=00, day_of_month=14), say_hello.s(), name="reset_data"
#     )
#
#
# @celery.task()
# def reset_data():
#     with create_app().app():
#         db.session.query(News).delete()
#         db.session.commit()

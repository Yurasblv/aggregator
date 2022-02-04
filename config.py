import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig():
    load_dotenv(os.path.join(basedir, ".dev_env"),override=True)
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")


class ProductionConfig():
    load_dotenv(os.path.join(basedir, ".prod_env"),override=True)
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = "True"
    SECRET_KEY = os.getenv("SECRET_KEY")
    CELERY_BROKER_URL = os.getenv("REDIS_URL")
    CELERY_RESULT_BACKEND = os.getenv("REDIS_URL")


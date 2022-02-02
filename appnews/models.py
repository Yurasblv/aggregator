import datetime
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort
db = SQLAlchemy()


class Contoller(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class User(UserMixin, db.Model):
    __tablename__ = "User"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=False)
    password = db.Column(
        db.String(200), primary_key=False, unique=False, nullable=False
    )
    created_on = db.Column(
        db.DateTime, index=False, unique=False, nullable=True, autoincrement=True
    )
    last_login = db.Column(
        db.DateTime, index=False, unique=False, nullable=True, autoincrement=True
    )
    is_admin = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return f"User data :{self.id}:{self.username}"

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        return check_password_hash(self.password, password)


class News(db.Model):

    __tablename__ = "News"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180))
    body = db.Column(db.Text(255))
    created_at = db.Column(db.DateTime)
    link = db.Column(db.String(200))
    author = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))

    def __repr__(self):
        return self.title

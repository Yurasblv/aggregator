from wtforms import SubmitField, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf import FlaskForm


class RegistrationForm(FlaskForm):
    username = StringField("Username", [Length(min=4, max=25)])
    password = PasswordField(
        "New Password",
        [
            DataRequired(),
            Length(min=6, message="Select a stronger password."),
            EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Repeat Password")


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Login")

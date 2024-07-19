from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField


class FeedbackForm(FlaskForm):
    feedback = StringField("feedback", validators=[validators.DataRequired()])


class SignUpForm(FlaskForm):
    nickname = StringField("Nickname", validators=[validators.DataRequired()])
    email = StringField("Email", validators=[
        validators.DataRequired(),
        validators.Email()
    ])
    password = StringField("password", validators=[
        validators.DataRequired(),
        validators.Length(min=4),
    ])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    nickname = StringField("Nickname", validators=[validators.DataRequired()])
    email = StringField("Email", validators=[
        validators.DataRequired(),
        validators.Email()
    ])
    password = PasswordField("password", validators=[
        validators.DataRequired(),
        validators.Length(min=4),
    ])
    submit = SubmitField("Login")

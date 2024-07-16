from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = 'your secret key'


class Base(DeclarativeBase):
    ...


dB = SQLAlchemy(model_class=Base)
dB.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "NEED LOGIN"
login_manager.init_app(app)




@login_manager.user_loader
def load_user(user_id: int):
    from .models import User
    user = dB.session.execute(dB.select(User).where(User.id == user_id)).scalar()
    # print(user)
    return user


from .routes import *

name = "Crave Pizza Corner"
schedule = "Будні: 8:00 - 21:00  " "Вихідні: 9:00 - 21:00"

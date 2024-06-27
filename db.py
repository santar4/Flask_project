from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app import app
from settings import *
# Створення двигуна, завдяки якому проводиться з'єднання з БД
engine = create_engine(
    app.config["DB_NAME"],
    echo=True,  # завдяки цьому аргументу буде виведення запитів у термінал(sys.stdout)
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# Створення конфігурації сесії на основі патерну Фабрика
Session = sessionmaker(bind=engine)




# Декларація базового класу для моделей
# Необхідно для реалізації відношень у ORM
class Base(DeclarativeBase):
    ...


dB = SQLAlchemy(model_class=Base)
dB.init_app(app)





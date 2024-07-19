from app import app

from app import dB
from app.models import Feedback, Pizza, User


def create_table():
    p1 = Pizza(name="Маргарита", description="Помідори, моцарела, базилік", prize=120)
    p2 = Pizza(name="Пепероні", description="Салямі, сир, томатний соус", prize=150)
    p3 = Pizza(name="Гавайська", description="Куряче філе, ананаси, шинка", prize=130)

    dB.session.add_all([p1, p2, p3])
    dB.session.commit()
    print("Data created")


with app.app_context():
    dB.create_all()
    print("Create db")
    create_table()

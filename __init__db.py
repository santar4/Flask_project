# from app import app
#
# from db import dB
# from app.models import Pizza
#
#
# def create_table():
#     p2 = Pizza(name="Пепероні", description="Салямі, сир, томатний соус", prize=120)
#
#     dB.session.add_all([p2])
#     dB.session.commit()
#     print("Data created")
#
#
# with app.app_context():
#     # dB.create_all()
#     print("Create db")
#     create_table()

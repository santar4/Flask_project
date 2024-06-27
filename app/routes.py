# from data import *




from flask import render_template
from flask_sqlalchemy import session
from sqlalchemy import  select
from app import app
from app.models import Pizza
from data.init import name, menu, schedule
from db import dB, Session


@app.route('/')
def home():
    return render_template("base.html",
                           title="Crave Pizza Corner",
                           time_work=schedule,
                           name=name
                           )


@app.route('/menu/')
def menu_page():
    stmt = select(Pizza)
    pizzas = dB.session.execute(stmt).scalars()
    context = {
        "title": "Menu",
        "name": "Ordername",
        "time_work": schedule

    }
    return render_template("Menu.html", pizzas=pizzas, **context)

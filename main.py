from pprint import pprint

from flask import Flask
from flask import render_template, redirect, abort

from data.data_db import get_all, create_table
from data.init import name, menu, schedule

app = Flask(__name__)




@app.route('/')
def home():
    return render_template("index.html",
                           title="Crave Pizza Corner",
                           time_work=schedule,
                           name=name
                            )


@app.route('/menu/')
def menu_page():
    menu_page = get_all()
    context = {
        "title": "Menu",
        "Menu": menu,
        "name": "Ordername",
        "time_work": schedule


    }
    pprint(menu_page)
    return render_template("Menu.html", **context, menu=menu)


if __name__ == "__main__":
    create_table()
    app.run(host='localhost', port=5050, debug=True)

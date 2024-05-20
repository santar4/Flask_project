from flask import Flask
from flask import render_template

app = Flask(__name__)

menu = [
    {"назва": "Маргарита", "опис": "Помідори, моцарела, базилік", "ціна": 100},
    {"назва": "Пепероні", "опис": "Салямі, сир, томатний соус", "ціна": 120},
    {"назва": "Гавайська", "опис": "Куряче філе, ананаси, шинка", "ціна": 130},
    {"назва": "М'ясна", "опис": "салямі, бекон, шинка, моцарела", "ціна": 130},
    {"назва": "Гавайська", "опис": "перець, гриби, оливки, моцарела", "ціна": 130}
]


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/menu/')
def menu_page():
    return render_template("Menu.html", menu=menu)


if __name__ == "__main__":
    app.run(host='localhost', port=5050, debug=True)

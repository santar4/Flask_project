from app import app

if __name__ == "__main__":

    # create_table()
    # menu_table = [
    #     {"name": "Маргарита", "description": "Помідори, моцарела, базилік", "prize": 100},
    #     {"name": "Пепероні", "description": "Салямі, сир, томатний соус", "prize": 120},
    #     {"name": "Гавайська Літня", "description": "Куряче філе, ананаси, шинка", "prize": 130},
    #     {"name": "М'ясна", "description": "салямі, бекон, шинка, моцарела", "prize": 130},
    #     {"name": "Гавайська", "description": "перець, гриби, оливки, моцарела", "prize": 130}
    # ]
    #
    # for d in menu_page:
    #     insert_data(**d)
    app.run(host='localhost', port=5050, debug=True)

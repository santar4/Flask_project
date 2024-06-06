import sqlite3
from datetime import datetime
from pprint import pprint

db_name = "database_menu3.db"


def make_read_query(query, *args):
    try:
        with sqlite3.connect(db_name) as conn:
            print(f"База данних {db_name} підключенна")
            cursor = conn.cursor()
            cursor.execute(query, *args)
            record = cursor.fetchall()

        return record

    except sqlite3.Error as e:
        print("Помилка запиту:", e)


def make_write_query(query, *args):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, *args)
            conn.commit()
            print("Запит записаний")

        print("Зєднання з SQLite закрите")
    except sqlite3.Error as e:
        print("Помилка запиту", e)


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS menu_page (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        prize INTEGER DEFAULT 0,  
        joining_date DATETIME);
    """
    make_write_query(query)
    print("table create")


def insert_data(name, description, prize=None):
    # joining_date = datetime.datetime.now()
    query = """
    INSERT INTO menu_page (name, description, prize)
               VALUES (?, ?, ?)
    """

    args = (name, description, prize)
    make_write_query(query, args)


def get_all():
    query = """SELECT * FROM menu_page"""
    return make_write_query(query)


def get_by_id(id):
    query = """SELECT * FROM menu_page WHERE id = ?"""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return {"id": result[0],
                "name": result[1],
                "description": result[2],
                "prize": result[3] if result[4] else 0,
                "data": result[4],
                }


def update_data_table(name, description, prize=None):
    # join_date = datetime.datetime.now()
    update_query = ("""
        UPDATE menu SET name = ?, description = ?, prize = ? 
        """)

    data_tuple = (name, description, prize,)
    make_write_query(update_query, data_tuple)


if __name__ == "__main__":
    # sqlite_select_query = "SELECT sqlite_version()"
    # record = make_read_query(sqlite_select_query)
    # print("Версія бази данних SQlite", record)
    #     print(f"База данних {db_name} підключенна")
    create_table()
    menu_page = [
        {"name": "Маргарита", "description": "Помідори, моцарела, базилік", "prize": 100},
        {"name": "Пепероні", "description": "Салямі, сир, томатний соус", "prize": 120},
        {"name": "Гавайська Літня", "description": "Куряче філе, ананаси, шинка", "prize": 130},
        {"name": "М'ясна", "description": "салямі, бекон, шинка, моцарела", "prize": 130},
        {"name": "Гавайська", "description": "перець, гриби, оливки, моцарела", "prize": 130}
    ]

    # for d in menu_page:
    #     insert_data(**d)

    pprint(get_all())

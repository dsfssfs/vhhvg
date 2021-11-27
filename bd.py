import sqlite3

connect = sqlite3.connect('all.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS subjects(
math text,
russian text,
chemistry text,
obg text,
obshestvo text,
geography text)

    """)
connect.commit()
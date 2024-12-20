import sqlite3 as sql

connection = sql.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
);
''')

# for i in range(1, 5):
#     cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
#                    (i, f'Продукт {i}', f'Описание продукта {i}', i*100))

connection.commit()
connection.close()

def get_all_products():
    connection = sql.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')

    result = cursor.fetchall()
    connection.close()

    return result

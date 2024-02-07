import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Створення таблиці для товарів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        name TEXT,
        price REAL,
        description TEXT
    )
''')

# Додавання першого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('✅115 VP🔥', 50, '❗VP - це внутрішня валюта у грі Valorant, розробленій компанією Riot Games'))

# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('✅485 VP🔥', 350, '❗VP - це внутрішня валюта у грі Valorant, розробленій компанією Riot Games'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🍂100 V-Bucks🌟', 15, '❗V-Bucks - це внутрішня валюта у грі Fortnite'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🍂200 V-Bucks🌟', 25, '❗V-Bucks - це внутрішня валюта у грі Fortnite'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🍂600 V-Bucks🌟', 55, '❗V-Bucks - це внутрішня валюта у грі Fortnite'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🍂1200 V-Bucks🌟', 100, '❗V-Bucks - це внутрішня валюта у грі Fortnite'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🍂3000 V-Bucks🌟', 299, '❗V-Bucks - це внутрішня валюта у грі Fortnite'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🍂5000 V-Bucks🌟', 349, '❗V-Bucks - це внутрішня валюта у грі Fortnite'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🧿100 Robux💫', 85, '❗Robux - це внутрішня валюта у грі Roblox'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🧿200 Robux💫', 150, '❗Robux - це внутрішня валюта у грі Roblox'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🧿500 Robux💫', 350, '❗Robux - це внутрішня валюта у грі Roblox'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🧿800 Robux💫', 420, '❗Robux - це внутрішня валюта у грі Roblox'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🧿1200 Robux💫', 700, '❗Robux - це внутрішня валюта у грі Roblox'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🧿1700 Robux💫', 885, '❗Robux - це внутрішня валюта у грі Roblox'))
# Додавання другого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('🧿2200 Robux💫', 970, '❗Robux - це внутрішня валюта у грі Roblox'))

def get_products():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT name, price FROM products''')
    products = cursor.fetchall()
    conn.close()
    return products

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()
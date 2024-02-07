import telebot
from telebot import types
import sqlite3

# Ідентифікатори адміністраторів бота
admin_ids = [123456789, 987654321]

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

# Створення таблиці для користувачів та їх балансу
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        balance REAL
    )
''')

# Додавання першого товару до бази даних
cursor.execute('''
    INSERT INTO products (name, price, description) VALUES (?, ?, ?)
''', ('✅115 VP🔥', 50, '❗VP - це внутрішня валюта у грі Valorant, розробленій компанією Riot Games'))

# Додавання грошей для користувачів
cursor.execute('''
    INSERT OR IGNORE INTO users (user_id, balance) VALUES (?, ?)
''', (admin_ids[0], 1000))  # Початковий баланс для адміністратора


# Додавання грошей для інших користувачів (якщо потрібно)
# cursor.execute('''
#     INSERT OR IGNORE INTO users (user_id, balance) VALUES (?, ?)
# ''', (user_id, initial_balance))

def get_products():
    cursor.execute('''SELECT name, price FROM products''')
    products = cursor.fetchall()
    return products


def get_user_balance(user_id):
    cursor.execute('''
        SELECT balance FROM users WHERE user_id = ?
    ''', (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None


def update_user_balance(user_id, new_balance):
    cursor.execute('''
        UPDATE users SET balance = ? WHERE user_id = ?
    ''', (new_balance, user_id))
    conn.commit()

bot = telebot.TeleBot('YOUR_BOT_TOKEN')  # Replace 'YOUR_BOT_TOKEN' with your actual token

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Ласкаво просимо! Ви можете поповнити свій рахунок, використовуючи команду /topup або вибрати товар зі списку /products.")


@bot.message_handler(commands=['topup'])
def topup_account(message):
    user_id = message.from_user.id

    if user_id not in admin_ids:
        bot.reply_to(message, "Вибачте, у вас немає доступу до цієї команди.")
        return

    markup = types.ForceReply(selective=False)
    bot.send_message(user_id, "Введіть суму для поповнення рахунку:", reply_markup=markup)


@bot.message_handler(commands=['balance'])
def check_balance(message):
    user_id = message.from_user.id
    balance = get_user_balance(user_id)

    if balance is not None:
        bot.reply_to(message, f"Ваш поточний баланс: {balance}")
    else:
        bot.reply_to(message, "Ваш баланс не знайдено. Зареєструйтеся командою /start або /topup.")

# Інші обробники повинні залишитися незмінними

if __name__ == "__main__":
    try:
        bot.polling(none_stop=True, interval=0, timeout=20, long_polling_timeout=5)
    except Exception as e:
        print(f"Error during polling: {e}")

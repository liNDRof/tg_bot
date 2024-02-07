from telebot import util
import telebot
from telebot import types
import sqlite3

# Токен вашого бота
TOKEN = '6858429939:AAGLKwYqmApDYj9HJaXItR4cL8aShR2pu5g'
bot = telebot.TeleBot(TOKEN)

# Ідентифікатори адміністраторів бота
admin_ids = [123456789, 987654321]

# Підключення до бази даних
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# ... (решта вашого коду)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def process_topup_or_purchase(message):
    user_id = message.from_user.id

    if user_id not in admin_ids:
        bot.reply_to(message, "Вибачте, у вас немає доступу до цієї команди.")
        return

    # Перевіряємо, чи є користувач у стані очікування оплати
    if user_id in user_states and user_states[user_id] == 'awaiting_payment':
        try:
            amount = float(message.text)
            # Тут ви можете виконати операцію поповнення рахунку та оновити баланс користувача
            # Наприклад, ви можете використовувати базу даних для збереження балансів користувачів.
            bot.send_message(user_id, f"Ваш рахунок поповнено на {amount}.")
        except ValueError:
            bot.send_message(user_id, "Будь ласка, введіть коректну суму.")
        finally:
            # Завершуємо стан очікування оплати
            del user_states[user_id]
    else:
        # Перевіряємо, чи користувач обрав товар
        products = get_products()
        selected_product = None
        for product in products:
            if f"{product[0]} - {product[1]}" == message.text:
                selected_product = product

        if selected_product:
            bot.send_message(user_id, f"Обраний товар: {selected_product[0]}\nЦіна: {selected_product[1]}")
            bot.send_message(admin_ids[0], f"Користувач {user_id} хоче купити товар {selected_product[0]}. "
                                           f"Будь ласка, введіть суму для оплати.")
            # Встановлюємо стан очікування оплати
            user_states[user_id] = 'awaiting_payment'

# ... (решта вашого коду)

if __name__ == "__main__":
    try:
        bot.polling(none_stop=True, interval=0, timeout=20, long_polling_timeout=5)
    except Exception as e:
        print(f"Error during polling: {e}")

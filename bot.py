import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6858429939:AAGLKwYqmApDYj9HJaXItR4cL8aShR2pu5g")
dp = Dispatcher()

available_buttons_step1 = ["Товари", "Налаштування", "Інфо"]


async def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*available_buttons_step1)
    return keyboard


@dp.message_handler(commands=('start'))
async def start(message: Message):
    keyboard = await get_keyboard()
    await message.answer("Виберіть опцію:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in available_buttons_step1)
async def handle_buttons_step1(message: Message):
    if message.text == "Товари":
        await message.answer("'Товари' тут")
    elif message.text == "Налаштування":
        await message.answer("'Налаштування' тут")
    elif message.text == "Інфо":
        await message.answer("'Інфо' тут")


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)

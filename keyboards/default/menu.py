from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сделать снимок"),
            KeyboardButton(text="Сигнализация"),
        ],
        [
            KeyboardButton(text="Температура"),
            KeyboardButton(text="Температура DHT11")
        ]
    ],
    resize_keyboard=True
)

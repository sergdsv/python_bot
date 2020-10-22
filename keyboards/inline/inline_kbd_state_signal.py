from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_kbd_signal_state = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Включить", callback_data="signal_on"),
            InlineKeyboardButton(text="Выключить", callback_data="signal_off")
        ],
        [
            InlineKeyboardButton(text="Статус", callback_data="signal_state"),
        ]
    ],
)

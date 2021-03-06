from loader import dp
from loader import bot
from aiogram.types import Message
from aiogram.dispatcher.filters import Text


def get_graph_temperature():
    contents = open('/home/pi/python/python_bot/raspberry_pi/temperature/temp_1d.png', 'rb')
    return contents


@dp.message_handler(Text(equals=["Температура", ]))
async def input_graph_temperature(message: Message):
    content = get_graph_temperature()
    await bot.send_photo(message.chat.id, content)

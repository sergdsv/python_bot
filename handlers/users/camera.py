from loader import dp
from loader import bot
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from subprocess import Popen, PIPE, STDOUT


def get_photo():
    p = Popen('/usr/bin/raspistill -t 500 -o /tmp/image.jpg -vf', shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    p.wait()
    contents = open('/tmp/image.jpg', 'rb')
    return contents


@dp.message_handler(Text(equals=["Сделать снимок", ]))
async def input_camera(message: Message):
    content = get_photo()
    await bot.send_photo(message.chat.id, content)

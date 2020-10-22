from loader import dp
from aiogram.types import Message
from keyboards.default import menu
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Menu", reply_markup=menu)

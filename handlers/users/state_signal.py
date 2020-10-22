from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from keyboards.inline import inline_kbd_signal_state
from aiogram.dispatcher import FSMContext
from gpiozero import MotionSensor
from .camera import get_photo
import asyncio

motion_detect = MotionSensor(5)


@dp.message_handler(Text(contains="Сигнализация"))
async def signal_menu(message: Message):
    await message.answer(message.text, reply_markup=inline_kbd_signal_state)


@dp.callback_query_handler(text_contains="signal_on")
async def signal_on(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['motion'] = 'on'
    await call.answer("Сигнализация включена!", show_alert=True)
    while True:
        data = await state.get_data()
        if data.get('motion') == 'on' and motion_detect.is_active:
            contents = get_photo()
            await dp.bot.send_photo(call.from_user.id, contents)
        await asyncio.sleep(10)


@dp.callback_query_handler(text_contains="signal_off")
async def signal_off(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['motion'] = 'off'
    await call.answer("Сигнализация выключена!", show_alert=True)


@dp.callback_query_handler(text_contains="signal_state")
async def signal_state(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data.get('motion') == 'on':
        await call.answer("Сигнализация включена!", show_alert=True)
    else:
        await call.answer("Сигнализация выключена!", show_alert=True)

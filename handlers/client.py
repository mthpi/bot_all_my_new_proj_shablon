from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
	await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)

# @dp.message_handler(commands=['Режим_работы'])
async def commands_open(message : types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

# @dp.message_handler(commands=['Расположение'])
async def commands_place(message : types.Message):
	await bot.send_message(message.from_user.id, 'ул. Колбасная 15')


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start', 'help'])
	dp.register_message_handler(commands_open, commands=['Режим_работы'])
	dp.register_message_handler(commands_place, commands=['Расположение'])

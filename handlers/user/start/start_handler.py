from aiogram import types, Router
from aiogram.filters import Command
from keyboard.inline_kb_generator import create_inline_kb
from aiogram.types import InlineKeyboardMarkup


# create a kb
kb: InlineKeyboardMarkup = create_inline_kb(2, 'current_load_list', "older_load_lists", 'carrier_list', 'add_load', 'add_carrier')

# create a router
start_router: Router = Router()


@start_router.message(Command(commands='start'))
async def bot_start_command(message: types.Message):
    await message.answer(f'HI, {message.from_user.first_name}', reply_markup=kb, parse_mode='html')
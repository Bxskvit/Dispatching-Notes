from aiogram import types, Router
from aiogram.filters import Command
from keyboard.inline_kb_generator import create_inline_kb
from aiogram.types import InlineKeyboardMarkup


# create a kb
# kb: InlineKeyboardMarkup = create_inline_kb(...)

# create a router
admin_start_router: Router = Router()


@admin_start_router.message(Command(commands='admin'))
async def bot_start_command(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, you\'ve entered admin mode', parse_mode='html')
from aiogram import Router
from states.User_states import AddLoadState
from aiogram.fsm.context import FSMContext
from keyboard.inline_kb_generator import create_inline_kb
from aiogram.types import InlineKeyboardMarkup, CallbackQuery
from aiogram import F

# create a kb
kb: InlineKeyboardMarkup = create_inline_kb(3, 'load_list', 'add_load')

# create a router
add_load_router: Router = Router()


@add_load_router.callback_query(F.data == "add_load")
async def add_load(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Let's add that load to the list! What's the <b>MC number of the company</b> you booked it for?", parse_mode='html')

    await state.set_state(AddLoadState.add_mc)

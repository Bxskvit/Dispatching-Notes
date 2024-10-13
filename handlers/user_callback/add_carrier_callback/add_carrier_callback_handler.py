from aiogram import Router
from states.User_states import AddCarrierState
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import F

# create a router
add_carrier_router: Router = Router()


@add_carrier_router.callback_query(F.data == "add_carrier")
async def add_load(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Let's add that Carrier! What's the <b>MC number of the company</b>?", parse_mode='html')

    await state.set_state(AddCarrierState.mc)

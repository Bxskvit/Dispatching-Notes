from states.User_states import AddLoadState
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from keyboard import create_inline_kb
from utils import Load
from database.database_utils import add_load

add_load_state_router: Router = Router()

kb = create_inline_kb(1, "setting_load_date_as_today")


@add_load_state_router.message(AddLoadState.add_mc)
async def process_mc(message: Message, state: FSMContext):
    await state.update_data(mc=message.text)
    await state.set_state(AddLoadState.pick_up)
    await message.reply("Where's the pickup?")


@add_load_state_router.message(AddLoadState.pick_up)
async def process_pick_up(message: Message, state: FSMContext):
    await state.update_data(pick_up=message.text)
    await state.set_state(AddLoadState.delivery)
    await message.reply("Where's the delivery?")


@add_load_state_router.message(AddLoadState.delivery)
async def process_delivery(message: Message, state: FSMContext):
    await state.update_data(delivery=message.text)
    await state.set_state(AddLoadState.mileage)
    await message.reply("What's the mileage of the trip?")


@add_load_state_router.message(AddLoadState.mileage)
async def process_mileage(message: Message, state: FSMContext):
    await state.update_data(mileage=message.text)
    await state.set_state(AddLoadState.date)
    await message.reply("What's the date of booking it?(you can simply click the 'It has been booked today')",
                        reply_markup=kb)


@add_load_state_router.message(AddLoadState.date)
async def process_date(message: Message, state: FSMContext):
    await state.update_data(date=message.text)
    await state.set_state(AddLoadState.load_number)
    await message.reply("What's the load number?")


@add_load_state_router.message(AddLoadState.load_number)
async def process_load_number(message: Message, state: FSMContext):
    await state.update_data(load_number=message.text)
    await state.set_state(AddLoadState.rate)
    await message.reply("What's the rate?")


@add_load_state_router.message(AddLoadState.rate)
async def process_rate(message: Message, state: FSMContext):
    await state.update_data(rate=message.text)

    # Retrieve the data from state
    data = await state.get_data()  # Use await here to get the stored data
    print(data)
    await message.reply("The Load has been added successfully")
    load = get_information(data=data)
    add_load(load=load)

    await state.clear()


def get_information(data):
    return Load(
        mc=data['mc'],
        pickup=data['pick_up'],
        delivery=data['delivery'],
        mileage=data['mileage'],
        date=data['date'],  # Corrected the key here to 'date'
        load_numebr=data['load_number'],  # Corrected the key here to 'load_number'
        rate=data['rate']
    )

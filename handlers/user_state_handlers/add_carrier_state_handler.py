from states.User_states import AddCarrierState
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from keyboard import create_inline_kb
from utils import Carrier
from database.database_utils import add_carrier

add_carrier_state_router: Router = Router()

kb = create_inline_kb(1, "cancel")


@add_carrier_state_router.message(AddCarrierState.mc)
async def process_mc(message: Message, state: FSMContext):
    await state.update_data(mc=message.text)
    await state.set_state(AddCarrierState.company_name)
    await message.reply("What's the company name?")


@add_carrier_state_router.message(AddCarrierState.company_name)
async def process_pick_up(message: Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    await state.set_state(AddCarrierState.hombase)
    await message.reply("Where's the hombase?")


@add_carrier_state_router.message(AddCarrierState.hombase)
async def process_delivery(message: Message, state: FSMContext):
    await state.update_data(hombase=message.text)
    await state.set_state(AddCarrierState.ph_number)
    await message.reply("What's the phone number?")


@add_carrier_state_router.message(AddCarrierState.ph_number)
async def process_mileage(message: Message, state: FSMContext):
    await state.update_data(ph_number=message.text)
    await state.set_state(AddCarrierState.email)
    await message.reply("What's the email?")


@add_carrier_state_router.message(AddCarrierState.email)
async def process_date(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(AddCarrierState.factoring)
    await message.reply("What's the factoring company?")


@add_carrier_state_router.message(AddCarrierState.factoring)
async def process_load_number(message: Message, state: FSMContext):
    await state.update_data(factoring=message.text)
    await state.set_state(AddCarrierState.name)
    await message.reply("What's the name of the owner?")


@add_carrier_state_router.message(AddCarrierState.name)
async def process_load_number(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddCarrierState.act_date)
    await message.reply("What's the MC activation date?")


@add_carrier_state_router.message(AddCarrierState.act_date)
async def process_rate(message: Message, state: FSMContext):
    await state.update_data(act_date=message.text)

    # Retrieve the data from state
    data = await state.get_data()  # Use await here to get the stored data
    await message.reply("The Carrier has been added successfully")
    carrier = get_information(data=data)
    add_carrier(carrier=carrier)

    await state.clear()


def get_information(data):
    return Carrier(
        mc=data['mc'],
        company_name=data['company_name'],
        hombase=data['hombase'],
        ph_number=data['ph_number'],
        email=data['email'],
        factoring=data['factoring'],
        name=data['name'],
        act_date=data['act_date']
    )

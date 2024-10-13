from aiogram.filters.state import State, StatesGroup


class AddLoadState(StatesGroup):
    add_mc = State()
    mileage = State()
    pick_up = State()
    delivery = State()
    date = State()
    load_number = State()
    rate = State()

from aiogram.filters.state import State, StatesGroup


class AddCarrierState(StatesGroup):
    mc = State()
    company_name = State()
    hombase = State()
    ph_number = State()
    email = State()
    factoring = State()
    name = State()
    act_date = State()

    # def __init__(self, mc: int, company_name: str, hombase: str, ph_number: int, email: str, factoring: str, name: str, act_date: str) -> None:
    #     self.mc = mc
    #     self.company_name = company_name
    #     self.hombase = hombase
    #     self.ph_number = ph_number
    #     self.email = email
    #     self.factoring = factoring
    #     self.name = name
    #     self.act_date = act_date
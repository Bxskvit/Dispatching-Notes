from utils import current_month_list

current_list = current_month_list()


async def create_list():
    with open(current_list, mode='w', newline='') as file:
        pass

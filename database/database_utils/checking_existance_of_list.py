from utils import wait_until_midnight
from .create_temporary_load_list import create_list


async def check_list_existence():
    await wait_until_midnight(func=create_list)


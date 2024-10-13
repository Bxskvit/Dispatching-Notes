from utils.set_monthly_timer import wait_until_next_month
from dropbox_utils import upload_file
from utils import previous_month_list
import os

list_location = previous_month_list()


async def close_existing_list():
    await wait_until_next_month(func=closing)


async def closing():
    upload_file(local_file_path=list_location)
    # os.remove(list_location)

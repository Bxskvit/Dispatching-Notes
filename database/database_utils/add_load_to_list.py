from utils import Load
import csv
from utils import current_month_list

current_list = current_month_list()


def add_load(load: Load) -> None:
    with open(current_list, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [load.mc, f'{load.pickup} to {load.delivery}', load.mileage, load.date, load.load_number, load.rate])

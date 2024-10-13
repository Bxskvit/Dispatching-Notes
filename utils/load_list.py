# from .load import Load
# import csv
# from tabulate import tabulate
# from shutil import move
# from datetime import datetime
#
#
# class LoadList:
#     load_table: list[Load] = []
#     total_rate = 0
#
#     def __init__(self) -> None:
#         self.month = self.get_month()
#         self.temporary_location = f'C:\\Users\\a\\PycharmProjects\\dsptchng_bot\\database\\temporary_data\\{self.month}_list.csv'
#         self.location = self.temporary_location
#
#     @staticmethod
#     def get_month() -> str:
#         return datetime.now().strftime("%B")
#
#     def count_total_rate(self):
#         for load in self.load_table:
#             self.total_rate += int(load.rate)
#
#     def add_load(self, load: Load) -> None:
#         self.load_table.append(load)
#         with open(self.location, mode='a', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(
#                 [load.mc, f'{load.pickup} to {load.delivery}', load.mileage, load.date, load.load_number, load.rate])
#
#     # def close_list(self) -> None:
#     #     # self.count_total_rate()
#     #     # with open(self.location, mode='a', newline='') as file:
#     #     #     writer = csv.writer(file)
#     #     #     writer.writerow(['Total rate', self.total_rate])
#     #     move(src=self.location, dst=self)
#
#     def __repr__(self):
#         pass
#
#
# def generate_load_list(src: LoadList) -> None:
#     headers = ['MC', 'Name of the comapany', 'Mileage', 'Date', 'Load number', 'Rate']
#     with open(src.location, mode='r') as file:
#         reader = csv.reader(file)
#         markdown = tabulate(reader, headers, tablefmt='pipe')
#     with open('loadlist.md', 'w') as file:
#         file.write(markdown)

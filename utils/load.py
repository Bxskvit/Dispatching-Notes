

class Load:
    def __init__(self, mc: int, rate: int, date: str, pickup:str, delivery: str, mileage: int, load_numebr: int) -> None:
        self.mc = mc
        self.rate = rate
        self.date = date
        self.pickup = pickup
        self.delivery = delivery
        self.mileage = mileage
        self.load_number = load_numebr

    def __repr__(self) -> str:
        return f'{self.pickup} to {self.delivery}, {self.rate}, {self.mc}'

    def add_load(self):
        return f'|{self.mc}|{self.pickup} to {self.delivery}|{self.date}|{self.load_number}|{self.rate}|'

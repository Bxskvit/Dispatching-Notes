

class Carrier:
    notes: list[str] = []

    def __init__(self, mc: int, company_name: str, hombase: str, ph_number: int, email: str, factoring: str, name: str, act_date: str) -> None:
        self.mc = mc
        self.company_name = company_name
        self.hombase = hombase
        self.ph_number = ph_number
        self.email = email
        self.factoring = factoring
        self.name = name
        self.act_date = act_date

    def add_note(self, conent: str) -> None:
        self.notes.append(conent)

    def to_csv_row(self) -> list:
        return [self.mc, self.company_name, self.hombase, self.ph_number, self.email,
                self.factoring, self.name, self.act_date, " | ".join(self.notes)]

    # def save_to_csv(self, file_name: str) -> None:
    #     # Append to an existing CSV file or create a new one if it doesn't exist
    #     with open(file_name, mode='a', newline='', encoding='utf-8') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(self.to_csv_row())


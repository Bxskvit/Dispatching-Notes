from utils import Carrier
from dropbox_utils import download_csv
from dropbox_utils import upload_csv


def add_carrier(file_path: str = "/Carriers/carriers.csv", carrier: Carrier = None) -> None:
    new_carrier = carrier.to_csv_row()
    # Download CSV from Dropbox
    rows = download_csv(file_path)

    # Append the new row
    rows.append(new_carrier)

    # Upload the modified CSV back to Dropbox
    upload_csv(file_path, rows)

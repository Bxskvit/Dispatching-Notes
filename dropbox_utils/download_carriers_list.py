from .dropbox_connection import connect_to_dropbox
import csv
from io import StringIO

dbx = connect_to_dropbox()


def download_csv(file_path: str = "/Carriers/carriers.csv") -> list:
    """Download the CSV file from Dropbox and return it as a list of rows."""
    _, res = dbx.files_download(file_path)
    file_data = res.content.decode('utf-8')

    # Reading CSV from Dropbox
    csv_reader = csv.reader(StringIO(file_data))
    rows = list(csv_reader)

    return rows

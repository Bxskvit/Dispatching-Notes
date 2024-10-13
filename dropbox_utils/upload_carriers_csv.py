from io import StringIO
import csv
from .dropbox_connection import connect_to_dropbox
from dropbox.files import WriteMode

dbx = connect_to_dropbox()


def upload_csv(file_path: str, rows: list) -> None:
    """Upload the modified CSV back to Dropbox."""
    output = StringIO()
    csv_writer = csv.writer(output)
    csv_writer.writerows(rows)

    # Upload the updated file back to Dropbox
    dbx.files_upload(output.getvalue().encode('utf-8'), file_path, mode=WriteMode.overwrite)


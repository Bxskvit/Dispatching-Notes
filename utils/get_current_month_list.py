import datetime
from config import TEMPORARY_DATA_FOLDER


def current_month_list():
    # Get the current date
    current_date = datetime.datetime.now()

    # Return the full month name (e.g., "October")
    month = current_date.strftime("%B")

    return f"{TEMPORARY_DATA_FOLDER}{month}_list.csv"

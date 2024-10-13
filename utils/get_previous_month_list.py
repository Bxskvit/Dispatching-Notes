import datetime
from config import TEMPORARY_DATA_FOLDER


def previous_month_list():
    # Get the current date
    current_date = datetime.datetime.now()

    # Calculate the previous month
    first_day_of_current_month = current_date.replace(day=1)
    last_day_of_previous_month = first_day_of_current_month - datetime.timedelta(days=1)

    # Return the full month name of the previous month (e.g., "September")
    last_month = last_day_of_previous_month.strftime("%B")
    return f"{TEMPORARY_DATA_FOLDER}{last_month}_list.csv"

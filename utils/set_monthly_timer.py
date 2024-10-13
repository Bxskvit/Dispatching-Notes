import datetime
import asyncio
from pytz import timezone


async def wait_until_next_month(func):
    # Time zone for Yerevan
    yerevan_tz = timezone('Asia/Yerevan')

    while True:
        # Get the current time in Yerevan time zone
        now = datetime.datetime.now(tz=yerevan_tz)

        # Calculate the first day of the next month at 1 PM in Yerevan time
        if now.month == 12:
            next_month = datetime.datetime(year=now.year + 1, month=1, day=1, hour=13, minute=0, second=0, tzinfo=yerevan_tz)
        else:
            next_month = datetime.datetime(year=now.year, month=now.month + 1, day=1, hour=13, minute=0, second=0, tzinfo=yerevan_tz)

        time_until_next_month = (next_month - now).total_seconds()

        # Sleep until 1 PM Yerevan time of the next month
        await asyncio.sleep(time_until_next_month)
        await func()

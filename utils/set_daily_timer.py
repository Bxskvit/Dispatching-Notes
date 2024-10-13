import time
import datetime
import asyncio


async def wait_until_midnight(func):
    await func()
    while True:
        # Get the current time
        now = datetime.datetime.now()

        # Calculate the time until the next midnight
        tomorrow = (now + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        time_until_midnight = (tomorrow - now).total_seconds()

        # Sleep until midnight

        await asyncio.sleep(time_until_midnight)
        await func()



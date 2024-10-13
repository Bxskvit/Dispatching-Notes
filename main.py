from bot import bot, dp
from database.database_utils import check_list_existence, close_existing_list
import asyncio
import handlers


async def start_database_services():
    await asyncio.gather(
        check_list_existence(),  # Call to check list existence
        close_existing_list()  # Call to close existing list
    )


async def run_bot():
    # Register routers
    dp.include_router(handlers.user.router)
    dp.include_router(handlers.user_callback.router)
    dp.include_router(handlers.admin.router)
    dp.include_router(handlers.user_state_handlers.router)

    print('Bot was started successfully!')
    # Start polling the bot (this should be awaited)
    await dp.start_polling(bot)


async def main():
    # Start database services and bot concurrently
    await asyncio.gather(
        start_database_services(),
        run_bot(),
    )


if __name__ == '__main__':
    try:
        # Try to get the current event loop
        loop = asyncio.get_event_loop()
    except RuntimeError as e:
        # If there is no event loop, create a new one
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Run the main function in the event loop
    loop.run_until_complete(main())

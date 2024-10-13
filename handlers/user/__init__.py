from aiogram import Router
from .start import start_router


# create a router
router: Router = Router()
router.include_router(router=start_router)


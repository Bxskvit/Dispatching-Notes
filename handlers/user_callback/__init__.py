from aiogram import Router
from .add_load_callback import add_load_router
from .add_carrier_callback import add_carrier_router

# create a router
router: Router = Router()
router.include_router(router=add_load_router)
router.include_router(router=add_carrier_router)

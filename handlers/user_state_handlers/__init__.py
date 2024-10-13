from aiogram import Router
from .add_load_state_handler import add_load_state_router
from .add_carrier_state_handler import add_carrier_state_router

# create a router
router: Router = Router()
router.include_router(router=add_load_state_router)
router.include_router(router=add_carrier_state_router)
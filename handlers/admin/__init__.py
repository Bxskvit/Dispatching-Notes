from aiogram import Router
from .admin_mode import admin_start_router

# create a router
router: Router = Router()
router.include_router(router=admin_start_router)
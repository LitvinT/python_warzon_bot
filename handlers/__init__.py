from aiogram import Router

from .users import users_router


router = Router(name='main')
router.include_router(router=users_router)


__all__: list[str] = [
    'router'
]

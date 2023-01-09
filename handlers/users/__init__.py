from aiogram import Router

from .model import user_model_router
from .main_panel import start_router
from .category import user_category_router
from .brand import user_brand_router
users_router = Router(name='users')
users_router.include_router(router=start_router)
users_router.include_router(router=user_category_router)
users_router.include_router(router=user_brand_router)
users_router.include_router(router=user_model_router)


__all__ = ('users_router',)
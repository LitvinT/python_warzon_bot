from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline.users import brand_paginator_ikb, brand_model_paginator_ikb
from keyboards.inline.users.general import UserCallbackData

user_brand_router = Router(name='user_category')


@user_brand_router.callback_query(UserCallbackData.filter((F.target == 'brand') & (F.action == 'page')))
async def paginate_categories(callback: CallbackQuery, callback_data: UserCallbackData):
    await callback.message.edit_text(
        text=('Выбери класс оружия 👇'),
        reply_markup=await brand_paginator_ikb(callback_data=callback_data)
    )


@user_brand_router.callback_query(UserCallbackData.filter((F.target == 'brand') & (F.action == 'get')))
async def get_category_products(callback: CallbackQuery, callback_data: UserCallbackData):
    await callback.message.edit_text(
        text='ВЫБЕРИТЕ МОДЕЛЬ 🔫',
        reply_markup=await brand_model_paginator_ikb(callback_data=callback_data)
    )


from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline.users import brand_model_paginator_ikb
from keyboards.inline.users.general import UserCallbackData

user_model_router = Router(name='user_model')


@user_model_router.callback_query(UserCallbackData.filter((F.target == 'model') & (F.action == 'page')))
async def paginate_brand(callback: CallbackQuery, callback_data: UserCallbackData):
    await callback.message.edit_text(
        text='ВЫБЕРИТЕ МОДЕЛЬ 🔫',
        reply_markup=await brand_model_paginator_ikb(callback_data=callback_data)
    )


@user_model_router.callback_query(UserCallbackData.filter((F.target == 'model') & (F.action == 'get')))
async def get_brand(callback: CallbackQuery, callback_data: UserCallbackData):
    await callback.message.edit_text(
        text='ВЫБЕРИТЕ ТОВАР',
        reply_markup=await brand_model_paginator_ikb(callback_data=callback_data)
    )
    # brand_model_paginator_ikb 23 строка
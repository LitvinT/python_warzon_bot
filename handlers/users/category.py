from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from keyboards.inline.users import category_paginator_ikb, brand_paginator_ikb
from keyboards.inline.users.general import UserCallbackData

user_category_router = Router(name='user_sex')


@user_category_router.message(F.text == '📲 Вызвать меню поиска сборки 🎮')
async def send_sex_ikb(message: Message):
    await message.delete()
    await message.answer(
        text='Выбери игру 👇',
        reply_markup=await category_paginator_ikb()
    )


@user_category_router.callback_query(UserCallbackData.filter((F.target == 'category') & (F.action == 'all')))
async def sex_panel(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Выбери игру 👇',
        reply_markup=await category_paginator_ikb()
    )


@user_category_router.callback_query(UserCallbackData.filter((F.target == 'category') & (F.action == 'get')))
async def get_sex(callback: CallbackQuery, callback_data: UserCallbackData):
    await callback.message.edit_text(
        text='Выбери класс оружия 👇',
        reply_markup=await brand_paginator_ikb(callback_data=callback_data)
    )


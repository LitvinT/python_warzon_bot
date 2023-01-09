from itertools import zip_longest

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from models import Category
from .general import UserCallbackData


async def category_paginator_ikb() -> InlineKeyboardMarkup:
    objs = await Category.all(is_published=True)
    objs_iter = iter(objs)
    objs_iter = list(map(list, zip_longest(*([objs_iter]*2))))
    buttons = [
        [
            InlineKeyboardButton(
                text=obj.category.upper(),
                callback_data=UserCallbackData(
                    target='category',
                    action='get',
                    sex_id=obj.id
                ).pack()
            )
            for obj in line
            if obj
        ]
        for line in objs_iter
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
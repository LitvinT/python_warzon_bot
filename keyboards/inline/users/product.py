from itertools import zip_longest

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from models import Product
from .general import UserCallbackData


async def product_paginator_ikb(callback_data: UserCallbackData) -> InlineKeyboardMarkup:
    filters_names = ('category_id', 'brand_id', 'model_id', )
    filters = dict(
        filter(
            lambda x: x[0] in filters_names and x[1], callback_data.dict().items()
        )
    )
    filters['is_published'] = True
    products = await Product.all(order_by='rating', **filters)

    buttons = []
    if products:
        products_iter = iter(products)
        products = list(zip_longest(*([products_iter] * 5)))
        products_page = list(filter(lambda x: x, products[callback_data.product_page]))
        buttons += [
            [
                InlineKeyboardButton(
                    text=product.name.upper(),
                    callback_data=UserCallbackData(
                        **callback_data.dict() | {
                            'target': 'product',
                            'action': 'get',
                            'product_id': product.id
                        }
                    ).pack()
                )
            ]
            for product in products_page
        ]
        if len(products) > 1:
            if not callback_data.product_page:
                prev_page = len(products) - 1
            else:
                prev_page = callback_data.product_page - 1

            if callback_data.product_page == len(products) - 1:
                next_page = 0
            else:
                next_page = callback_data.product_page + 1

            buttons += [
                [
                    InlineKeyboardButton(
                        text='⬅️',
                        callback_data=UserCallbackData(
                            **callback_data.dict() | {
                                'target': 'product',
                                'action': 'page',
                                'product_page': prev_page
                            }
                        ).pack()
                    ),
                    InlineKeyboardButton(
                        text='➡️',
                        callback_data=UserCallbackData(
                            **callback_data.dict() | {
                                'target': 'product',
                                'action': 'page',
                                'product_page': next_page
                            }
                        ).pack()
                    )
                ]
            ]
    buttons += [
        [
            InlineKeyboardButton(
                text='🔙',
                callback_data=UserCallbackData(
                    **callback_data.dict() | {
                        'target': 'model',
                        'action': 'page',
                    }
                ).pack()
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)



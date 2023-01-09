from aiogram import F, Router
from aiogram.types import Message

from keyboards.replay import main_panel_kb
from models import User

start_router = Router(name='start')


@start_router.message(F.text == '/start')
async def command_start(message: Message):
    await message.delete()
    if await User.get(pk=message.from_user.id):
        await message.answer(
            text=f'🤩ПРИВЕТСТВУЮ ВАС!🖐️. {message.from_user.full_name}',
            reply_markup=main_panel_kb)
    else:
        user = User(id=message.from_user.id, name=message.from_user.full_name)
        await user.save()
        await message.answer(
            text=f'🤩ПРИВЕТСТВУЮ ВАС!🖐️. {message.from_user.full_name}',
            reply_markup=main_panel_kb
        )




if __name__ == '__main__':
    from handlers import router
    from loader import bot, dp

    dp.include_router(router=router)
    dp.run_polling(bot)
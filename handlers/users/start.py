import pysqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default import lesson
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    # Foydalanuvchini bazaga qoshamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        count = db.count_users()[0]
        msg = f'<a href="tg://user?id={user_id}">{name}</a> bazaga qoshildi. \nBazada {count} ta foydalanuvchi bor.' \
              f'\nID {user_id}.'
        await bot.send_message(chat_id=ADMINS[1], text=msg)
        await message.answer(f"Assalomu aleykum, {message.from_user.full_name}!\n"
                             f"IT sohasiga doir foydali va samarali bo'lgan bepul darslarni ulashuvchi botga xush kelibsiz.", reply_markup=lesson)

    except pysqlite3.IntegrityError as err:
        await message.answer(f"Sizni yana ko'rganimizdan xursandmiz 😊 .")
        # await bot.send_message(chat_id=ADMINS[0], text=err)
        pass

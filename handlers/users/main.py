import asyncio

from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from handlers.Lessons.css import CSS
from handlers.Lessons.html import HTML
from keyboards.default import lesson
from loader import dp


@dp.message_handler(content_types="video")
async def return_videoid(msg: types.Message):
    await msg.reply(msg.video.file_id)


@dp.message_handler(text="HTML")
async def return_video(message: types.Message):
    for cap, video in HTML.items():
        await message.answer_video(video, caption=f'📹{cap}\n\n© @UlugbekSamigjonov\n\nFoydali va samarali video darslar:\n@DolphinLessonsBot 🐬',
                                   reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(0.1)
    await message.answer("""Ulug'bek Samigjonov - HTML darslari 29 qismdan iborat
    
Foydali va samarali video darslar:
@DolphinLessonsBot 🐬""", reply_markup=lesson)


@dp.message_handler(text='CSS')
async def dsasdasd(message: types.Message):
    for cap, video in CSS.items():
        await message.answer_video(video, caption=f'📹{cap}\n\n© @UlugbekSamigjonov\n\nFoydali va samarali video darslar:\n@DolphinLessonsBot 🐬',
                                   reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(0.1)
    await message.answer("""Ulug'bek Samigjonov - CSS darslari 63 qismdan iborat

    Foydali va samarali video darslar:
    @DolphinLessonsBot 🐬""", reply_markup=lesson)



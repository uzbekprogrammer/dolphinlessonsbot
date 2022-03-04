import asyncio

from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from handlers.Lessons.css import CSS
from handlers.Lessons.django import DJANGO
from handlers.Lessons.html import HTML
from handlers.Lessons.javascript import JAVASCRIPT
from handlers.Lessons.python import PYTHON
from handlers.Lessons.sass import SASS
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


@dp.message_handler(text='SASS')
async def sass(message: types.Message):
    for cap, video in SASS.items():
        await message.answer_video(video, caption=f'📹{cap}\n\n© @UlugbekSamigjonov\n\nFoydali va samarali video darslar:\n@DolphinLessonsBot 🐬',
                                   reply_markup=ReplyKeyboardRemove())

        await asyncio.sleep(0.1)
    await message.answer("""Ulug'bek Samigjonov - SASS darslari 18 qismdan iborat

Foydali va samarali video darslar:
@DolphinLessonsBot 🐬""", reply_markup=lesson)


@dp.message_handler(text='JavaScript')
async def sass(message: types.Message):
    for cap, video in JAVASCRIPT.items():
        await message.answer_video(video, caption=f'📹{cap}\n\n© @UlugbekSamigjonov\n\nFoydali va samarali video darslar:\n@DolphinLessonsBot 🐬',
                                   reply_markup=ReplyKeyboardRemove())

        await asyncio.sleep(0.1)
    await message.answer("""Ulug'bek Samigjonov - JavaScript darslari 15 qismdan iborat

Foydali va samarali video darslar:
@DolphinLessonsBot 🐬""", reply_markup=lesson)


@dp.message_handler(text='Django')
async def sass(message: types.Message):
    for cap, video in DJANGO.items():
        await message.answer_video(video, caption=f'📹{cap}\n\n© Anvar Narzullayev\n\nFoydali va samarali video darslar:\n@DolphinLessonsBot 🐬',
                                   reply_markup=ReplyKeyboardRemove())

        await asyncio.sleep(0.1)
    await message.answer("""Anvar Narzullayev - Python Django darslari 25 qismdan iborat

Foydali va samarali video darslar:
@DolphinLessonsBot 🐬""", reply_markup=lesson)


@dp.message_handler(text='Python')
async def sass(message: types.Message):
    for cap, video in PYTHON.items():
        await message.answer_video(video, caption=f'📹{cap}\n\n© Anvar Narzullayev\n\nFoydali va samarali video darslar:\n@DolphinLessonsBot 🐬',
                                   reply_markup=ReplyKeyboardRemove())

        await asyncio.sleep(0.1)
    await message.answer("""Anvar Narzullayev - Python Django darslari 25 qismdan iborat

Foydali va samarali video darslar:
@DolphinLessonsBot 🐬""", reply_markup=lesson)


@dp.message_handler(text='Python | TelegramBot')
async def sass(message: types.Message):
    for cap, video in PYTHON.items():
        await message.answer_video(video, caption=f'📹{cap}\n\n© Anvar Narzullayev\n\nFoydali va samarali video darslar:\n@DolphinLessonsBot 🐬',
                                   reply_markup=ReplyKeyboardRemove())

        await asyncio.sleep(0.1)
    await message.answer("""Anvar Narzullayev - Python TelegramBot darslarini bepul qismi 13 qismdan iborat

Foydali va samarali video darslar:
@DolphinLessonsBot 🐬""", reply_markup=lesson)

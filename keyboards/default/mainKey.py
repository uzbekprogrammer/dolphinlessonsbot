from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lesson = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="HTML"),
            KeyboardButton(text="CSS"),
        ],
        [
            KeyboardButton(text="Bootstrap"),
            KeyboardButton(text="SASS")
        ],
        [
            KeyboardButton(text="JavaScript")
        ],
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="Django")
        ],
        [
            KeyboardButton(text="Python | TelegramBot"),
            KeyboardButton(text="")
        ]


    ],
    resize_keyboard=True
)

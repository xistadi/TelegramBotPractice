from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Котлетки"),
        ],
        [
            KeyboardButton(text="Макарошки"),
            KeyboardButton(text="Пюрешка")
        ],
        [
            KeyboardButton(text='Kekw')
        ]
    ],
    resize_keyboard=True
)

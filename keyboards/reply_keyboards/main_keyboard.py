from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_buttons = [
    [KeyboardButton(text="Profile"), KeyboardButton(text="Map pool")],
    [KeyboardButton(text="Statistics")]
]

main_keyboard = ReplyKeyboardMarkup(
    keyboard=main_buttons,
    resize_keyboard=True
)
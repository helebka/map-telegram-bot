from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

maps_buttons = [
    [KeyboardButton(text="Nuke"), KeyboardButton(text="Vertigo")],
    [KeyboardButton(text="Inferno"), KeyboardButton(text="Overpass")]
]

maps_keyboard = ReplyKeyboardMarkup(
    keyboard=maps_buttons,
    resize_keyboard=True
)

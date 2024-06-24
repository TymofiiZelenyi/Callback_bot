import aiogram
from .callback_buttons import button1, button2

inline_keyboard = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard= [
        [button1, button2] #Порядок розставланнея buttons
    ]
)


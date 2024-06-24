import aiogram
from .dispatcher_bot import dispatcher
import aiogram.filters 
from .inline_keyboards import inline_keyboard

command_start = aiogram.filters.CommandStart()

@dispatcher.message(command_start)
async def start(message: aiogram.types.Message): #Функція реагує на команду /start
    await message.answer(text = "Hello, User!", reply_markup = inline_keyboard)
import aiogram
from .dispatcher_bot import dispatcher

@dispatcher.callback_query()
async def callback_handler(callback: aiogram.types.CallbackQuery):
    if "1" in callback.data:
        await callback.message.answer(text= "Натиснута кнопка 1")  #Якщо користувач натискає на інлайн кнопку button_1 or button_2 то тоді бот відповідає йому
    if "2" in callback.data:
        await callback.message.answer(text= "Натиснута кнопка 2")

from .dispatcher_bot import dispatcher
from .create_bot import bot

async def main(): #запускає проект у дію
    await dispatcher.start_polling(bot) #запускає проект у дію
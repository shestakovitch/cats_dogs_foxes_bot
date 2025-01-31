import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from config import Config, load_config
import user_handlers

# logger initializing
logger = logging.getLogger(__name__)


async def set_main_menu(bot: Bot):
    # create a command list
    main_menu_commands = [
        BotCommand(command="/start",
                   description="Bot starting")
    ]

    await bot.set_my_commands(main_menu_commands)


# configuration function and launching the bot
async def main():
    # configuring logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    # output information about the start of the bot launch to the console
    logger.info('Starting bot')

    # load the config into the config variable
    config: Config = load_config()

    # initialize the bot and dispatcher
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # registering router in the dispatcher
    dp.include_router(user_handlers.router)

    # register an asynchronous function in the dispatcher, which will be executed on bot startup
    dp.startup.register(set_main_menu)

    # skip the backlog of updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())

# standart lib
import asyncio
import logging

# files system
from config import load_config

# aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# middlewares
from middlewares.anti_time import Anti_time

# handlers
from handlers.start import register_start
from handlers.help import register_help
from misc.default_commands import set_commands
from handlers.community import register_community
from handlers.profile import register_profile

logger = logging.getLogger(__name__)


def register_all_middleware(dp):
    dp.setup_middleware(Anti_time())


def register_all_handlers(dp):
    register_start(dp)
    register_help(dp)
    register_community(dp)
    register_profile(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s'
    )

    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config  # доставать config из переменной bot, если в handler я хочу достать что то из Config
    # я делаю => bot.get("config")

    register_all_middleware(dp)
    # register_all_fillters(dp)
    register_all_handlers(dp)
    try:
        await dp.start_polling()
        await set_commands(bot=bot)
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await dp.bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stop")

    executor.start_polling(dp, skip_updates=True)

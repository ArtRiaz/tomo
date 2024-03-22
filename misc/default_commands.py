from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, WebAppInfo


# default menu

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='🏁 Start the bot'),
        BotCommand(command='profile', description='👤 Profile'),
        BotCommand(command='help', description='🆘 Show help'),
        BotCommand(command='referral', description='👥 Invite a friend'),
        BotCommand(command='contact', description='📞 Contact us'),
        # BotCommand(command='leaderboard', description='Leaderboard'),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

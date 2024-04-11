from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, WebAppInfo


# default menu

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='profile', description='👤 Profile'),
        BotCommand(command='rules', description='📋 Rules of the game'),
        BotCommand(command='referral', description='👥 Invite a friend'),
        BotCommand(command='social', description='📲 Social'),
        # BotCommand(command='leaderboard', description='Leaderboard'),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

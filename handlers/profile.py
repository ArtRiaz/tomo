from aiogram import types, Bot, Dispatcher
from random import randint
import random

# Helper functions

prize = random.choice(["🏆 Bronze League", "🥈 Silver League",
                       "🥇 Gold League", "🏅 Platinum League", "💎 Diamond League"])
num = randint(0, 100)


async def cmd_profile(message: types.Message):
    await message.answer(f"{message.from_user.full_name} profile\n "
                         "\n"
                         f"{prize}\n"
                         f"\n"
                         f"🪙 Total score: {num}\n"
                         "\n"
                         f"🪙 Balance: {num}\n")


def register_profile(dp: Dispatcher):
    dp.register_message_handler(cmd_profile, commands="profile")

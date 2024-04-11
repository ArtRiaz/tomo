from aiogram import types, Bot, Dispatcher
from data.db import User
from aiogram.utils.markdown import hlink, hbold, hcode
from config import load_config
import aiohttp

"""User Interface results of the leaderboard and profile results."""


# Рассмотрите возможность инициализации сессии вне этих функций, если она используется многократно
session = None


async def get_session():
    global session
    if session is None or session.closed:
        session = aiohttp.ClientSession()
    return session


async def get_profile(url, headers):
    session = await get_session()
    async with session.get(url, headers=headers) as response:
        if response.status == 404:
            return None
        return await response.json()


async def cmd_profile(message: types.Message):
    conf = load_config()
    chat_id = message.from_user.id
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        results = await get_profile(f"https://admin.{conf.misc.domain}/api/telegram-id/{chat_id}", headers=headers)

        if results is None:
            await message.answer(f"👤 <b>Profile: Not found\nRegister your profile.</b>")
            return

        balance = results.get("wallet_balance", 0) or 0
        await message.answer_photo(open('static/profile.png', 'rb'),
                                   caption=f"👤 Profile: {message.from_user.username}\n\n🏆 Total balance: {balance}")

    except aiohttp.ClientError as e:
        print(e)
        await message.answer("Oops... something went wrong\nYour profile is not available at the moment.\n"
                             "Please try again ...")


# Не забудьте закрыть сессию при завершении работы


# leaderboards


# async def cmd_leaderboard(message: types.Message):
#     # Open a session and get data from the server.
#     with open('static/profile.png', 'rb') as photo:
#         try:
#             s = requests.Session()
#             headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, "
#                                      "like Gecko)"
#                                      " Version/16.5.2 Safari/605.1.15"}
#
#             res = s.get(f"https://admin.prodtest1.space/api/telegram-id/{message.from_user.id}", headers=headers)
#             results = res.json()
#             print(results)
#             print(results['wallet_address'])
#
#             response = s.get(f"https://admin.prodtest1.space/api/liderbord/{results['wallet_address']}",
#                              headers=headers)
#             res = response.json()
#             # print(f"Status: {response.status_code}")
#             # print(f"Content: {response.json()}")
#
#             response_text = "\n\n".join(
#                 [
#                     f"{hbold(user['position'])}. {hbold(user['wallet_address'])} {user['wallet_name']} "
#                     f"{hcode(user['wallet_balance'])}\n"
#                     for user in res
#                 ]
#             )
#
#             await message.answer(response_text.strip())
#
#         except requests.exceptions.RequestException as e:
#             print(e)
#             await message.answer("Error: {e}")


def register_profile(dp: Dispatcher):
    dp.register_message_handler(cmd_profile, commands="profile")
    # dp.register_message_handler(cmd_leaderboard, commands="leaderboard")

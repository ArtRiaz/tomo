from aiogram import types, Bot, Dispatcher
import requests
from data.db import User
from aiogram.utils.markdown import hlink, hbold, hcode
from keyboards.inline import back_keyboard
from config import load_config

"""User Interface results of the leaderboard and profile results."""


# Profile

async def cmd_profile(message: types.Message):
    conf = load_config()
    # Open a session and get data from the server.
    with open('static/profile.png', 'rb') as photo:
        try:
            s = requests.Session()
            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, "
                                     "like Gecko)"
                                     " Version/16.5.2 Safari/605.1.15"}

            res = s.get(f"https://admin.{conf.misc.domain}/api/telegram-id/{message.from_user.id}", headers=headers)
            results = res.json()
            print(results)

            if results == 404:
                await message.answer(f"👤 <b>Profile: Not found\n"
                                     f"Register your profile.</b>")
            else:
                await message.answer_photo(photo, f"👤 Pofile: {message.from_user.username}\n"
                                                  "\n"
                                                  f"🏆 Total balance: {results['wallet_balance']}\n"
                                           )
        except requests.exceptions.RequestException as e:
            print(e)
            await message.answer("Opps... what went wrong\n"
                                 "Your profile is not available at the moment.\n"
                                 " Please try again, click 👉 /start")


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

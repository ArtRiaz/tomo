import requests
import json
import asyncio
import aiohttp

from aiogram import types, Bot
from aiogram.utils.deep_linking import get_start_link
import config
from keyboards.inline import start_keyboard, play_game, start_keyboard_user
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from data.db import DBCommands, create_db, User
from config import load_config

db = DBCommands()
conf = load_config()

"""Start the bot. This is the first message that the user sees when he starts the bot
The user is offered to register his wallet to play the game.
Create a new user in the database.
Check if the user is in the web database
If the user is in the database, the user is offered to play the game.
If the user is not in the database, the user is offered to register his wallet to play the game."""


# Open session and get data from the server
async def get_start(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # print(f"Status: {response.status}")
            # print(f"Content: {await response.json()}")
            return await response.json()


# start

async def start(message: types.Message):
    with open('static/Frame_51441632.jpg', 'rb') as photo:

        # Create a database
        await create_db()

        # take chat_id
        chat_id = message.from_user.id


        # Save user and refferals to the database
        # Take arguments from the message link "https://t.me/tim_cat_bot?start={args}"
        refferal = message.get_args()

        # Add a new user to the database and check if the user is in the database
        # Add refferal to the database
        await db.add_new_user(refferal)

        """Open a session and post data to the server."""

        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, "
                                 "like Gecko)"
                                 " Version/16.5.2 Safari/605.1.15"}

        response = await get_start(f"https://admin.{conf.misc.domain}/api/telegram-id/{chat_id}", headers=headers)
        # "https://admin.prodtest1.space/api/telegram-id/1064938479"

        # Fetch user data asynchronously

        check_user = response
        print(check_user)
        if check_user == 404:
            text = (f"<b>Hey, {message.from_user.full_name} 👋!\n\n"
                    f"📦 Introducing Tim the Cat, homeless cat found under a "
                    f"cardboard box.\n\n"
                    f"Bring him home, care for him, and watch as he becomes "
                    f"happier,"
                    f"bringing you more rewards as a loyal companion.\n\n"
                    f"🎮 Game Mechanics: feed, play, pet, and groom Tom to earn "
                    f"rewards.\n\n"
                    f"💰 Blockchain: a decentralized and hyped memecoin on the "
                    f"Solana"
                    f"blockchain.\n\n"
                    f"🎁 Bonuses: invite friends to unlock boosters and more "
                    f"rewards.\n\n"
                    f"📲 Join a heartwarming Telegram bot game with exciting "
                    f"rewards and a "
                    f"touching story and get rewarded for your kindness!</b>")

            await message.answer_photo(photo=photo, caption=text,
                                       reply_markup=start_keyboard())

        else:
            text = (f"<b>Hey, {message.from_user.full_name} 👋!\n\n"
                    f"📦 Introducing Tim the Cat, homeless cat found under a "
                    f"cardboard box.\n\n"
                    f"Bring him home, care for him, and watch as he becomes "
                    f"happier,"
                    f"bringing you more rewards as a loyal companion.\n\n"
                    f"🎮 Game Mechanics: feed, play, pet, and groom Tom to earn "
                    f"rewards.\n\n"
                    f"💰 Blockchain: a decentralized and hyped memecoin on the "
                    f"Solana"
                    f"blockchain.\n\n"
                    f"🎁 Bonuses: invite friends to unlock boosters and more "
                    f"rewards.\n\n"
                    f"📲 Join a heartwarming Telegram bot game with exciting "
                    f"rewards and a "
                    f"touching story and get rewarded for your kindness!</b>")
            await message.answer_photo(photo=photo, caption=text,
                                       reply_markup=start_keyboard_user())


"""Register to play"""


class RegisterPlay(StatesGroup):
    wallet_address = State()


"""Cancel registration your wallet for the game"""


async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Cancellation of registaration for the game", reply_markup=types.ReplyKeyboardRemove())
    await state.reset_state()


"""Start registration your wallet for the game,
Add a wallet name  for the game
"""


async def play_wallet_name(call: types.CallbackQuery):
    await call.message.answer("<b>In order to play the game, you need to register your wallet 💳.\n"
                              "You can use any wallet that supports the Solana network.\n"
                              "If you cancel the registration, click the </b>👉/cancel")
    # sleep(4)
    await asyncio.sleep(3)

    await call.message.answer("<b>Create your wallet address 🔑 that supports"
                              " the Solana network, for example: phantom, solflare,"
                              "metamask, trezor: or click</b> /cancel")
    await RegisterPlay.wallet_address.set()


"""Post  wallet address to the server"""


# name = message.text


async def post_wallet(message: types.Message, state: FSMContext):
    wallet_address = message.text
    register = User()
    register.wallet_address = wallet_address

    chat_id = message.from_user.id

    invite_ref = await db.get_user(chat_id)

    # Fill in the database
    await state.update_data(register=register)
    await register.create()

    """Open a session and post data to the server."""

    async with aiohttp.ClientSession() as session:
        # take chat_id
        chat_id = message.from_user.id

        if invite_ref is None:

            data_post = {
                "wallet_address": wallet_address,
                "wallet_name": "",
                "id_telegram": chat_id,
                "parent_id_telegram": ""
            }

        else:
            # data for post with refferal
            data_post = {
                "wallet_address": wallet_address,
                "wallet_name": "",
                "id_telegram": chat_id,
                "parent_id_telegram": invite_ref.refferal
            }
        url = f"https://admin.{conf.misc.domain}/api/users"

        headers = {
            "Content-type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)"
                          "Version/16.5.2 Safari/605.1.15",
        }

        async with session.post(url, json=data_post, headers=headers) as response:
            if response.ok:
                await message.answer("<b>Your wallet has been successfully registered 📲.\n"
                                     "Remember your key 🔑 and don't give it to anyone</b>", reply_markup=play_game())
            else:
                await message.answer(f"<b>Oppps... something went wrong\n"
                                     f"Your wallet has not been registered.\n"
                                     f"Please try again, click</b> 👉 /start")

        await state.finish()


# refferral

async def refferal(message: types.Message):
    with (open('static/referal.png', 'rb') as photo):
        # refferal = await db.check_referrals()
        deep_link = await get_start_link(payload=message.from_user.id)
        await message.answer_photo(photo=photo, caption=f"<b>🔗 Your referral link:\n{deep_link}\n"
                                                        f"🎁 Invite friends and get bonuses!</b>",
                                   reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[
                                       types.InlineKeyboardButton(text="Invite friends",
                                                                  switch_inline_query=f"Hey my friend!\n"
                                                                                      f"Join for a new game with Tim "
                                                                                      f"the Cat!\n"
                                                                                      f"🔗 {deep_link}")
                                   ]]))


def register_start(dp):
    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(cancel, commands=["cancel"], state=RegisterPlay)
    dp.register_callback_query_handler(play_wallet_name, text="play")
    dp.register_message_handler(post_wallet, state=RegisterPlay.wallet_address)
    dp.register_message_handler(refferal, commands="referral")

import requests
import json
import asyncio
import aiohttp
import config

from aiogram import types, Bot
from aiogram.utils.deep_linking import get_start_link
from keyboards.inline import start_keyboard, play_game, start_keyboard_user, start_game, play_game_new_ref
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


# Open the session GET request

async def get_user(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # print(f"Status: {response.status}")
            # print(f"Content: {await response.json()}")
            return response.status


# start
# Check referral. Try to request the referral from api
async def start(message: types.Message):
    with open('static/start.png', 'rb') as photo:
        # Create a database
        await create_db()

        # take chat_id
        chat_id = message.from_user.id  # -> 1234567

        # It's new user

        # Save user and refferals to the database
        # Take arguments from the message link "https://t.me/tim_cat_bot?start={args}"
        referral = message.get_args()

        # Add a new user to the database and check if the user is in the database
        # Add refferal to the database
        await db.add_new_user(referral)
        referral_id = await db.get_user(chat_id)

        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, "
                                 "like Gecko)"
                                 " Version/16.5.2 Safari/605.1.15"}

        results = await get_user(f"https://admin.{conf.misc.domain}/api/telegram-id/{chat_id}",
                                 headers=headers)

        if results == 404:
            print("No user found")
            async with aiohttp.ClientSession() as session:
                # Open session and post data to the api
                if referral_id.refferal is not None:
                    print("Referral")
                    # take chat_id
                    chat_id = message.from_user.id

                    # send post request to the api with parent_id_telegram and id_telegram
                    data_post = {
                        "id_telegram": chat_id,
                        "parent_id_telegram": referral_id.refferal
                    }

                else:
                    print("No referral")

                    # send post request to the api with id_telegram
                    data_post = {
                        "id_telegram": chat_id,
                    }

                url = f"https://admin.{conf.misc.domain}/api/users"

                headers = {
                    "Content-type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, "
                                  "like Gecko)"
                                  "Version/16.5.2 Safari/605.1.15",
                }

                async with session.post(url, json=data_post, headers=headers) as response:
                    print(response.status)

                text = (f"<b>Hey, {message.from_user.full_name} 👋!\n\n"
                        f"🐈‍⬛ Let me introduce myself — I’m Tomo, a stray cat.\n\n"
                        f"Tired and sad, I gain magical powers when you take care of me.\n\n"
                        f"🐾 Just pet me and I’ll bring your rewards.\n\n"
                        f"To boost them, think about my food, style, and fun..\n\n"
                        f"🐾 Also, surround me with your friends. A meow fam purrs with more bonuses!</b>")

                await message.answer_photo(photo=photo, caption=text,
                                           reply_markup=start_keyboard())

        else:
            print("User in database")
            text = (f"<b>Hey, {message.from_user.full_name} 👋!\n\n"
                    f"🐈‍⬛ Let me introduce myself — I’m Tomo, a stray cat.\n\n"
                    f"Tired and sad, I gain magical powers when you take care of me.\n\n"
                    f"🐾 Just pet me and I’ll bring your rewards.\n\n"
                    f"To boost them, think about my food, style, and fun..\n\n"
                    f"🐾 Also, surround me with your friends. A meow fam purrs with more bonuses!</b>")

            await message.answer_photo(photo=photo, caption=text,
                                       reply_markup=start_keyboard_user())

        # /api/users


"""New user"""


# We need to request the referral address ->
async def play_game_user(callback: types.CallbackQuery):
    # Take the user's referral address
    refferal_id = await db.get_user(callback.from_user.id)
    print(refferal_id.refferal)

    # Check if the user has a referral address
    if refferal_id.refferal is not None:
        print("Referral")
        await callback.message.answer(f"<b>{callback.from_user.full_name} 👋! Let's play the game\n"
                                      f"Choice your status:</b>", reply_markup=play_game_new_ref())
    else:
        print("No referral")
        await callback.message.answer(f"<b>{callback.from_user.full_name} 👋! Let's play the game\n"
                                      f"Choice your status:</b>", reply_markup=start_game())


"""Register to play"""


class RegisterPlay(StatesGroup):
    wallet_address = State()


"""Cancel registration your wallet for the game"""


async def cancel(message: types.Message, state: FSMContext):
    with open('static/start.png', 'rb') as photo:
        await message.answer("<b>Cancellation of validation for the game</b>")
        await asyncio.sleep(3)
        text = (f"<b>Hey, {message.from_user.full_name} 👋!\n\n"
                f"🐈‍⬛ Let me introduce myself — I’m Tomo, a stray cat.\n\n"
                f"Tired and sad, I gain magical powers when you take care of me.\n\n"
                f"🐾 Just pet me and I’ll bring your rewards.\n\n"
                f"To boost them, think about my food, style, and fun..\n\n"
                f"🐾 Also, surround me with your friends. A meow fam purrs with more bonuses!</b>")
        await message.answer_photo(photo=photo, caption=text,
                                   reply_markup=start_keyboard())
        await state.reset_state()


"""Start registration your wallet for the game,1
Add a wallet name  for the game
"""


async def play_wallet_name(call: types.CallbackQuery):
    await call.message.answer("<b>🐾 Are you new to Telegram?\n"
                              "Let’s get a wallet."
                              "👉You can also</b> /cancel")
    # sleep(4)
    await asyncio.sleep(3)

    await call.message.answer(f"<b>🐈‍⬛ Enter your wallet and we’ll start playing.\n"
                              "👉You can also</b> /cancel 💳")
    await RegisterPlay.wallet_address.set()


"""Post  wallet address to the server"""


async def post_wallet(message: types.Message, state: FSMContext):
    with open('static/start.png', 'rb') as photo:
        wallet_address = message.text
        register = User()
        register.wallet_address = wallet_address

        # Fill in the database
        await state.update_data(register=register)
        await register.create()

        """Open a session and post data to the server."""

        async with aiohttp.ClientSession() as session:
            # take chat_id
            chat_id = message.from_user.id

            data_post = {
                "wallet_address": wallet_address,
                "wallet_name": "",
                "id_telegram": chat_id,
            }

            url = f"https://admin.{conf.misc.domain}/api/users"

            headers = {
                "Content-type": "application/json",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)"
                              "Version/16.5.2 Safari/605.1.15",
            }

            async with session.post(url, json=data_post, headers=headers) as response:
                if response.status == 404:
                    print(response.status)
                    await message.answer(f"<b>Oops! Seems like you have no wallet in our database 🤯\n"
                                         f"Let’s create a new one!\n"
                                         f"Get a Solana-based "
                                         f"<a href='https://solflare.com/'>Solflare</a>,"
                                         f" <a href='https://phantom.app'>Phantom</a>, "
                                         f"<a href='https://metamask.io'>Metamask</a>, or"
                                         f" <a href='https://trezor.io'>Trezor</a> 💳\n"
                                         f"Please try again ...</b>")
                    await asyncio.sleep(3)
                    text = (f"<b>Hey, {message.from_user.full_name} 👋!\n\n"
                            f"🐈‍⬛ Let me introduce myself — I’m Tomo, a stray cat.\n\n"
                            f"Tired and sad, I gain magical powers when you take care of me.\n\n"
                            f"🐾 Just pet me and I’ll bring your rewards.\n\n"
                            f"To boost them, think about my food, style, and fun..\n\n"
                            f"🐾 Also, surround me with your friends. A meow fam purrs with more bonuses!</b>")
                    await message.answer_photo(photo=photo, caption=text,
                                               reply_markup=start_keyboard())
                else:
                    print(response.status)
                    await message.answer(f"<b>DOPE! Everything is OK 👯\n"
                                         f"Hear me purr</b>"
                                         , reply_markup=play_game_new_ref())

        await state.finish()


# refferral link

async def refferal(message: types.Message):
    with (open('static/referal.png', 'rb') as photo):
        deep_link = await get_start_link(payload=message.from_user.id)
        await message.answer_photo(photo=photo, caption=f"<b>🔗 Your link:\n{deep_link}\n"
                                                        f"🎁 Invite friends and get 10% of their revenues</b>",
                                   reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[
                                       types.InlineKeyboardButton(text="Invite",
                                                                  switch_inline_query=f"Hey my friend!\n"
                                                                                      f"Join for a new game with Tomo "
                                                                                      f"the Cat!\n"
                                                                                      f"🔗 {deep_link}")
                                   ]]))


def register_start(dp):
    dp.register_message_handler(start, commands="start")
    dp.register_callback_query_handler(play_game_user, text="play")
    dp.register_message_handler(cancel, commands=["cancel"], state=RegisterPlay)
    dp.register_callback_query_handler(play_wallet_name, text="register")
    dp.register_message_handler(post_wallet, state=RegisterPlay.wallet_address)
    dp.register_message_handler(refferal, commands="referral")

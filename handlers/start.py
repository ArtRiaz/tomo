import requests
import json
import asyncio
import aiohttp
import config
import logging
import time

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

async def get_user(session, url, headers):
    async with session.get(url, headers=headers) as response:
        return response.status


async def post_user(session, url, headers, data_post):
    async with session.post(url, json=data_post, headers=headers) as response:
        print(response.status)


async def start(message: types.Message):
    # Создание клиентской сессии внутри асинхронной функции
    async with aiohttp.ClientSession() as session:
        with open('static/start.png', 'rb') as photo:
            # One time download
            await create_db()
            chat_id = message.from_user.id

            refferal = message.get_args()
            await db.add_new_user(refferal)
            referral_id = await db.get_user(chat_id)

            headers = {
                "Content-type": "application/json",
                "User-Agent": "Mozilla/5.0"
            }

            results = await get_user(session, f"https://admin.{conf.misc.domain}/api/telegram-id/{chat_id}", headers)

            if results == 404:
                print('User no found')
                data_post = {
                    "id_telegram": chat_id,
                    "parent_id_telegram": referral_id.refferal if referral_id.refferal else None
                }
                await post_user(session, f"https://admin.{conf.misc.domain}/api/users", headers, data_post)
            else:
                print("User in database")

            text = "<b>Hey, {name} 👋!\n\n".format(name=message.from_user.full_name) + \
                   "🐈‍⬛ Let me introduce myself — I’m Tomo, a stray cat.\n\n" + \
                   "🐾 Just pet me and I’ll bring your rewards.\n\n" + \
                   "To boost them, think about my food, style, and fun..\n\n" + \
                   "🐾 Also, surround me with your friends. A meow fam purrs with more bonuses!</b>"

            keyboard = start_keyboard_user() if results != 404 else start_keyboard()
            await message.answer_photo(photo=photo, caption=text, reply_markup=keyboard)
            await message.delete()


# /api/users


"""New user"""


# We need to request the referral address ->

async def play_game_user(callback: types.CallbackQuery):
    try:
        # Получаем referral_id пользователя
        referral_id = await db.get_user(callback.from_user.id)
        logging.info(f"User {callback.from_user.id} referral: {referral_id.refferal}")

        # Определяем, есть ли у пользователя реферальный адрес
        reply_markup = play_game_new_ref() if referral_id.refferal else start_game()
        message_text = f"<b>{callback.from_user.full_name} 👋! Let's play the game\nChoice your status:</b>"

        # Отправляем сообщение пользователю с выбранной клавиатурой
        await callback.message.answer(message_text, reply_markup=reply_markup)
        await callback.message.edit_reply_markup()
    except Exception as e:
        logging.error(f"Error in play_game_user: {e}")
        # Здесь можно добавить отправку сообщения об ошибке пользователю, если это необходимо


"""Register the wallet address"""


class RegisterPlay(StatesGroup):
    wallet_address = State()


async def cancel(message: types.Message, state: FSMContext):
    await message.answer("<b>OK, I get you. Let’s return to the game 🎮</b>")
    await asyncio.sleep(4)
    await message.delete()
    await send_introduction(message, "Let’s return to the game 🎮")
    await state.reset_state()


async def play_wallet_name(call: types.CallbackQuery):
    await call.message.answer("<b>Continue playing with the wallet you’ve already used 🐈‍⬛\nEnter your Solana Wallet "
                              "address\n👉You can also</b> /cancel")
    await RegisterPlay.wallet_address.set()


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
                                         f"<a href='https://phantom.app'>Phantom</a>,"
                                         f"<a href='https://solflare.com'>Solflare</a>\n"
                                         f"Please try again ...</b>")
                    await asyncio.sleep(4)
                    text = (f"<b>Hey, {message.from_user.full_name} 👋!\n\n"
                            f"🐈⬛ Let me introduce myself — I’m Tomo, a stray cat.\n\n"
                            f"Tired and sad, I gain magical powers when you take care of me.\n\n"
                            f"🐾 Just pet me and I’ll bring your rewards.\n\n"
                            f"To boost them, think about my food, style, and fun..\n\n"
                            f"🐾 Also, surround me with your friends. A meow fam purrs with more bonuses!</b>")
                    await message.answer_photo(photo=photo, caption=text,
                                               reply_markup=start_keyboard())
                    await message.delete()
                else:
                    print(response.status)
                    await message.answer(f"<b>DOPE! Everything is OK 👯\n"
                                         f"Hear me purr</b>"
                                         , reply_markup=play_game_new_ref())
                    await message.delete()

        await state.finish()


# refferral link

async def referral(message: types.Message):
    deep_link = await get_start_link(payload=str(message.from_user.id))
    invite_text = "Invite"
    invite_callback = f"Hey my friend!\nJoin for a new game with Tomo the Cat!\n🔗 {deep_link}"

    keyboard = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text=invite_text, switch_inline_query=invite_callback))

    caption = (f"<b>🔗 Your link:\n{deep_link}\n"
               f"🎁 Invite friends and get 10% of their revenues</b>")

    with open('static/referal.png', 'rb') as photo:
        await message.answer_photo(photo=photo, caption=caption, reply_markup=keyboard)


def register_start(dp):
    dp.register_message_handler(start, commands="start")
    dp.register_callback_query_handler(play_game_user, text="play")
    dp.register_message_handler(cancel, commands=["cancel"], state=RegisterPlay)
    dp.register_callback_query_handler(play_wallet_name, text="register")
    dp.register_message_handler(post_wallet, state=RegisterPlay.wallet_address)
    dp.register_message_handler(referral, commands="referral")

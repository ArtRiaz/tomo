from aiogram import types, Bot
from keyboards.inline import start_keyboard

#from data.db import DBCommands, create_db


#db = DBCommands()


# start

async def start(message: types.Message):
    with open('tomas.jpeg', 'rb') as photo:
#        await create_db()

        chat_id = message.from_user.id
#        await db.add_new_user()

        await message.bot.send_photo(chat_id=chat_id, photo=photo,
                                     caption=f"Hey, {message.from_user.full_name}! Welcome to Crypto Tom!\n"
                                             "Tap on the coin and see your balance rise.\n"

                                             "Crypto Tom is a Decentralized Exchange on the Solana Blockchain. The "
                                             "biggest part of "
                                             "Crypto Tom Token TAPS distribution"
                                             "will occur among the players here.\n"
                                             "n"
                                             "Got friends, relatives, co-workers?\n"
                                             "Bring them all into the game.\n"
                                             "More buddies, more coins.", reply_markup=start_keyboard())


#refferral

async def refferal(message: types.Message):
    user = await db.add_new_user()
    ref_link = f"https://t.me/tom_crypto_bot?start={user.user_id}"
    await message.answer(f"Your referral link: {ref_link}")


def register_start(dp):
    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(refferal, commands="referral")

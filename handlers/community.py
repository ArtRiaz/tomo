from aiogram import types, Bot, Dispatcher
from keyboards.inline import community_keyboard


# Community functions

async def cmd_community(call: types.CallbackQuery):
    with open('static/Contacts.png', 'rb') as photo:
        await call.message.answer_photo(photo, "<b>Join our socials so "
                                               "you do not miss any important news or updates.</b>",
                                        reply_markup=community_keyboard())

        await call.message.delete()


# Contacts list

async def cmd_contact(message: types.Message):
    with open('static/Contacts.png', 'rb') as photo:
        await message.answer_photo(photo, "<b>Join our socials so "
                                          "you do not miss any important news or updates.</b>",
                                   reply_markup=community_keyboard())

        await message.delete()


def register_community(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_community, text="community")
    dp.register_message_handler(cmd_contact, commands="contact")

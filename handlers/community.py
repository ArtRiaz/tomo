from aiogram import types, Bot, Dispatcher
from keyboards.inline import community_keyboard


# Community functions

async def cmd_community(call: types.CallbackQuery):
    with open('tomas.jpeg', 'rb') as photo:
        await call.message.answer_photo(photo, "Join our socials so "
                                               "you do not miss any important news or updates.",
                                        reply_markup=community_keyboard())

        await call.message.delete()


def register_community(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_community, text="community")

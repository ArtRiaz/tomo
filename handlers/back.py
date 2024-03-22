from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.inline import start_keyboard, start_keyboard_user

# New user back button

async def cmd_back(call: types.CallbackQuery):
    with open('tomas.jpeg', 'rb') as photo:
        await call.message.delete()
        await call.message.answer_photo(photo, 'You come back in Main menu:',
                                        reply_markup=start_keyboard())

# Back old

async def cmd_back_old(call: types.CallbackQuery):
    with open('tomas.jpeg', 'rb') as photo:
        await call.message.delete()
        await call.message.answer_photo(photo, 'You come back in Main menu:',
                                        reply_markup=start_keyboard_user())

def register_handler_back(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_back, text="back_new")
    dp.register_callback_query_handler(cmd_back_old, text="back_old")

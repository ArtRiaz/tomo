from aiogram import types, Bot, Dispatcher
from keyboards.inline import back_keyboard


# Helper functions

async def cmd_help(message: types.Message):
    with open('tomas.jpeg', 'rb') as photo:
        await message.answer_photo(photo, "This is help message\n "
                                          "You'll need to add your content here", reply_markup=back_keyboard())


async def help(call: types.CallbackQuery):
    with open('tomas.jpeg', 'rb') as photo:
        await call.message.answer_photo(photo, "This is help message\n "
                                               "You'll need to add your content here", reply_markup=back_keyboard())
        await call.message.delete()


def register_help(dp: Dispatcher):
    dp.register_message_handler(cmd_help, commands="help")
    dp.register_callback_query_handler(help, text="help")

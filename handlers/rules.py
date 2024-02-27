from aiogram import types, Bot, Dispatcher
from keyboards.inline import back_keyboard

# Rules of the game

async def cmd_rules(message: types.Message):
    with open('tomas.jpeg', 'rb') as photo:
        await message.answer_photo(photo, "This are rules message\n "
                                          "You'll need to add your content here", reply_markup=back_keyboard())


def register_rules(dp: Dispatcher):
    dp.register_message_handler(cmd_rules, commands="rules")

from aiogram import types, Bot, Dispatcher

# Helper functions

from aiogram import types, Bot, Dispatcher

CAPTION = ("<b>How to pet me?\n\n"
           "🎮 Play\n"
           "Tap the screen, make me purr, and get rewards.\n\n"
           "💸 Gain\n"
           "Climb the leaderboard and gain more.\n\n"
           "🚀 Boost\n"
           "Skyrocket your rewards with boosts.\n\n"
           "💌 Invite\n"
           "Bring friends and get bonuses for their success.\n\n"
           "🎁 Party\n"
           "Stay active and enjoy extra rewards.</b>")


async def send_help(target, is_callback_query=False):
    with open('static/rules.png', 'rb') as photo:
        if is_callback_query:
            await target.message.answer_photo(photo, caption=CAPTION)
            await target.message.delete()
        else:
            await target.answer_photo(photo, caption=CAPTION)
            await target.delete()


async def cmd_help(message: types.Message):
    await send_help(message)


async def help_handler(call: types.CallbackQuery):
    await send_help(call, is_callback_query=True)


def register_help(dp: Dispatcher):
    dp.register_message_handler(cmd_help, commands="rules")
    dp.register_callback_query_handler(help, text="rules")

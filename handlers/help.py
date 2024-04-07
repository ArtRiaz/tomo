from aiogram import types, Bot, Dispatcher


# Helper functions

async def cmd_help(message: types.Message):
    with open('static/rules.png', 'rb') as photo:
        await message.answer_photo(photo, caption="<b>How to pet me?\n\n"
                                                  "🎮 Play\n"
                                                  "Tap the screen, make me purr, and get rewards.\n\n"

                                                  "💸 Gain\n"
                                                  "Climb the leaderboard and gain more.\n\n"

                                                  " 🚀 Boost\n"
                                                  "Skyrocket your rewards with boosts.\n\n"

                                                  "💌 Invite\n"
                                                  "Bring friends and get bonuses for their success.\n\n"

                                                  "🎁 Party\n"
                                                  "Stay active and enjoy extra rewards.</b>")


async def help(call: types.CallbackQuery):
    with open('static/rules.png', 'rb') as photo:
        await call.message.answer_photo(photo, caption="<b>How to pet me?\n\n"
                                                       "🎮 Play\n"
                                                       "Tap the screen, make me purr, and get rewards.\n\n"

                                                       "💸 Gain\n"
                                                       "Climb the leaderboard and gain more.\n\n"

                                                       " 🚀 Boost\n"
                                                       "Skyrocket your rewards with boosts.\n\n"

                                                       "💌 Invite\n"
                                                       "Bring friends and get bonuses for their success.\n\n"

                                                       "🎁 Party\n"
                                                       "Stay active and enjoy extra rewards.</b>")
        await call.message.delete()


def register_help(dp: Dispatcher):
    dp.register_message_handler(cmd_help, commands="rules")
    dp.register_callback_query_handler(help, text="rules")

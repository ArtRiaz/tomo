from aiogram import types, Bot, Dispatcher
from keyboards.inline import back_keyboard


# Helper functions

async def cmd_help(message: types.Message):
    with open('static/Help.png', 'rb') as photo:
        await message.answer_photo(photo, "<b>How to play?\n\n"

                                          "🎮 Game mechanics: tap to earn, Tom the Cat is an addictive clicker game "
                                          "where you accumulate rewards by tapping the"
                                          "screen.\n\n"

                                          "🏆 Leagues: Climb the ranks by earning more rewards and outperforming others "
                                          "in the leagues.\n\n"

                                          "🚀 Boosts: Unlock boosts and complete tasks to maximize your rewards "
                                          "earnings.\n\n"

                                          "👥 Friends: Invite others and both of you will receive bonuses. Assist your "
                                          "friends in advancing to higher leagues for bigger rewards.\n\n"

                                          "🎁 We have provided more valuable rewards for the most active users! Show "
                                          "your love for Tim the cat and he will reward you well!</b>")


async def help(call: types.CallbackQuery):
    with open('static/Help.png', 'rb') as photo:
        await call.message.answer_photo(photo, "<b>How to play?\n\n"

                                               "🎮 Game mechanics: tap to earn, Tom the Cat is an addictive clicker "
                                               "game"
                                               "where you accumulate rewards by tapping the"
                                               "screen.\n\n"

                                               "🏆 Leagues: Climb the ranks by earning more rewards and outperforming "
                                               "others"
                                               "in the leagues.\n\n"

                                               "🚀 Boosts: Unlock boosts and complete tasks to maximize your rewards "
                                               "earnings.\n\n"

                                               "👥 Friends: Invite others and both of you will receive bonuses. "
                                               "Assist your"
                                               "friends in advancing to higher leagues for bigger rewards.\n\n"

                                               "🎁 We have provided more valuable rewards for the most active users! "
                                               "Show"
                                               "your love for Tom the cat and he will reward you well!</b>")
        await call.message.delete()


def register_help(dp: Dispatcher):
    dp.register_message_handler(cmd_help, commands="help")
    dp.register_callback_query_handler(help, text="help")

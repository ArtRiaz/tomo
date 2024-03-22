from aiogram import types, Bot, Dispatcher
from keyboards.inline import back_keyboard


# Rules of the game

async def cmd_rules(message: types.Message):
    with open('static/Frame_51441632.jpg', 'rb') as photo:
        await message.answer_photo(photo, "<b>How to play?\n\n"

                                          "Game mechanics: tap to earn, Tom the Cat is an addictive clicker game "
                                          "where you accumulate rewards by tapping the"
                                          "screen.\n"

                                          "Leagues: Climb the ranks by earning more rewards and outperforming others "
                                          "in the leagues.\n"

                                          "Boosts: Unlock boosts and complete tasks to maximize your rewards "
                                          "earnings.\n"

                                          "Friends: Invite others and both of you will receive bonuses. Assist your "
                                          "friends in advancing to higher leagues for bigger rewards.\n"

                                          "We have provided more valuable rewards for the most active users! Show "
                                          "your love for Tom the cat and he will reward you well!</b>")


def register_rules(dp: Dispatcher):
    dp.register_message_handler(cmd_rules, commands="rules")

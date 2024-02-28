from aiogram import types, Bot, Dispatcher
from keyboards.inline import back_keyboard


# Rules of the game

async def cmd_rules(message: types.Message):
    with open('tomas.jpeg', 'rb') as photo:
        await message.answer_photo(photo, "Tap to earn\n"
                                          "Notcoin is a viral clicker game where you earn coins by tapping on the screen.\n"
                                          "\n"
                                          "Leagues\n"
                                          "The more coins you earn, the higher you will be in the leagues.\n"
                                          "\n"
                                          "Boosts\n"
                                          "Get boosts and complete tasks to earn more Notcoins.\n"
                                          "\n"
                                          "Frens\n"
                                          "Invite someone, and you both receive bonuses. Help a friend move to the next league,"
                                          " and you will get even more Notcoin bonuses.\n"
                                          "\n"
                                          "Squads\n"
                                          "Telegram channels and groups are Squads; join them to play with others."
                                          " Those invited to the squad via your link are counted as your referrals.\n"
                                          "\n"
                                          "Wen\n"
                                          "No one knows if the Notcoin token will be released and when that will happen."
                                          " No one knows if it will be worth anything or not.\n"
                                          "\n"
                                          "And that's the whole charm.\n"

                                          "Let's find out together.", reply_markup=back_keyboard())


def register_rules(dp: Dispatcher):
    dp.register_message_handler(cmd_rules, commands="rules")

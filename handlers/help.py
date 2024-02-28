from aiogram import types, Bot, Dispatcher
from keyboards.inline import back_keyboard


# Helper functions

async def cmd_help(message: types.Message):
    with open('tomas.jpeg', 'rb') as photo:
        await message.answer_photo(photo, "Tap to Earn:\n"
                                          "TapSwap is an addictive clicker game where you accumulate Shares by "
                                          "tapping the screen."
                                          "\n"
                                          "Leagues:\n"
                                          "Climb the ranks by earning more Shares and outperforming others in the "
                                          "leagues."
                                          "\n"
                                          "Boosts:\n"
                                          "Unlock boosts and complete tasks to maximize your Shares earnings."

                                          "Friends:\n"
                                          "Invite others and both of you will receive bonuses. Assist your friends in "
                                          "advancing to higher leagues"
                                          " for bigger Shares rewards."
                                          "\n"
                                          "The Purpose:\n"
                                          "Collect as many Shares as possible and exchange them for TAPS, TapSwap "
                                          "Token on Solana Blockchain.",
                                   reply_markup=back_keyboard())


async def help(call: types.CallbackQuery):
    with open('tomas.jpeg', 'rb') as photo:
        await call.message.answer_photo(photo, "Tap to Earn:\n"
                                          "TapSwap is an addictive clicker game where you accumulate Shares by "
                                          "tapping the screen."
                                          "\n"
                                          "Leagues:\n"
                                          "Climb the ranks by earning more Shares and outperforming others in the "
                                          "leagues."
                                          "\n"
                                          "Boosts:\n"
                                          "Unlock boosts and complete tasks to maximize your Shares earnings."

                                          "Friends:\n"
                                          "Invite others and both of you will receive bonuses. Assist your friends in "
                                          "advancing to higher leagues"
                                          " for bigger Shares rewards."
                                          "\n"
                                          "The Purpose:\n"
                                          "Collect as many Shares as possible and exchange them for TAPS, TapSwap "
                                          "Token on Solana Blockchain.", reply_markup=back_keyboard())
        await call.message.delete()


def register_help(dp: Dispatcher):
    dp.register_message_handler(cmd_help, commands="help")
    dp.register_callback_query_handler(help, text="help")

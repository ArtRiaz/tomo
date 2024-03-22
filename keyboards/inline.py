from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# Keyboards

# New user
def start_keyboard():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play now!",
                              callback_data="play")], [
            InlineKeyboardButton(text="👥 Join community", callback_data="community")
        ],
        [InlineKeyboardButton(text="🆘 Help", callback_data="help")]
    ]
    )
    return ikb


# Old user

def start_keyboard_user():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play now!",
                              web_app=WebAppInfo(url="https://www.prodtest1.space/"))], [
            InlineKeyboardButton(text="👥 Join community", callback_data="community")
        ],
        [InlineKeyboardButton(text="🆘 Help", callback_data="help")]
    ]
    )
    return ikb


def community_keyboard():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Telegram", url="https://t.me/Crypto_Cat_Tom")],
        [InlineKeyboardButton(text="Twitter", url="https://twitter.com/TimCatSol")]
    ]
    )
    return ikb


def back_keyboard():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="back")]
    ]
    )
    return ikb




def play_game():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play now!", web_app=WebAppInfo(url="https://www.prodtest1.space/"))],
    ]
    )
    return ikb




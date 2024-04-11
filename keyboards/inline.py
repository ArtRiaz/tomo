from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# Keyboards

# New user
def start_keyboard():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play", callback_data="play")], [
            InlineKeyboardButton(text="👯 Community", callback_data="community")],

        [InlineKeyboardButton(text="📋 Rules", callback_data="rules")]
    ]
    )
    return ikb


# Old user

def start_keyboard_user():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play now",
                              web_app=WebAppInfo(url="https://nvadim11.github.io/TommyTg/"))], [
            InlineKeyboardButton(text="👯 Community", callback_data="community")
        ],
        [InlineKeyboardButton(text="📋 Rules", callback_data="rules")]
    ]
    )
    return ikb


def community_keyboard():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Telegram", url="https://t.me/tomocat_sol")],
        [InlineKeyboardButton(text="Twitter", url="https://twitter.com/TimCatSol")]
    ]
    )
    return ikb


def play_game():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play now", web_app=WebAppInfo(url="https://nvadim11.github.io/TommyTg/"))],
    ]
    )
    return ikb


def start_game():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play now", web_app=WebAppInfo(url="https://nvadim11.github.io/TommyTg/"))],
        [InlineKeyboardButton(text="📲 Log in with a wallet", callback_data="register")],
    ]
    )
    return ikb


def play_game_new_ref():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play", web_app=WebAppInfo(url="https://nvadim11.github.io/TommyTg/"))],
        [InlineKeyboardButton(text="📋 Rules", callback_data="rules")]
    ]
    )

    return ikb

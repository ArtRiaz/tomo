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
        [InlineKeyboardButton(text="🎮 Play",
                              web_app=WebAppInfo(url="https://5db0-212-178-0-123.ngrok-free.app/"))], [
            InlineKeyboardButton(text="👯 Community", callback_data="community")
        ],
        [InlineKeyboardButton(text="📋 Rules", callback_data="rules")]
    ]
    )
    return ikb


def community_keyboard():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Telegram", url="https://t.me/tomo_cat")],
        [InlineKeyboardButton(text="Twitter", url="https://twitter.com/TimCatSol")]
    ]
    )
    return ikb


def play_game():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play", web_app=WebAppInfo(url="https://5db0-212-178-0-123.ngrok-free.app/"))],
    ]
    )
    return ikb


def start_game():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 A newbie", web_app=WebAppInfo(url="https://5db0-212-178-0-123.ngrok-free.app/"))],
        [InlineKeyboardButton(text="📲 A player", callback_data="register")],
    ]
    )
    return ikb


def play_game_new_ref():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play", web_app=WebAppInfo(url="https://5db0-212-178-0-123.ngrok-free.app/"))],
        [InlineKeyboardButton(text="📋 Rules", callback_data="rules")]
    ]
    )

    return ikb

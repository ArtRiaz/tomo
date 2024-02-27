from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton


# Keyboards
def start_keyboard():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Play now!",
                              web_app=WebAppInfo(url="https://nvadim11.github.io/CryptoTom/dist/index.html"))], [
            InlineKeyboardButton(text="Join community", callback_data="community")
        ],
        [InlineKeyboardButton(text="Help", callback_data="help")]
    ]
    )
    return ikb


def community_keyboard():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Telegram", url="https://t.me/Crypto_Cat_Tom")],
        [InlineKeyboardButton(text="Discord", url="https://discord.gg/3vzD2K7q")],
        [InlineKeyboardButton(text="Instagram", url="https://www.instagram.com")],
        [InlineKeyboardButton(text="Back", callback_data="back")]
    ]
    )
    return ikb


def back_keyboard():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Back", callback_data="back")]
    ]
    )
    return ikb


def play_keyboard():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Play now!", callback_data="play")]
    ]
    )
    return ikb

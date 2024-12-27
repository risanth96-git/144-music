import re
from pyrogram import filters
import random
from AmritaXMusic import app


@app.on_message(filters.command(["gm","m","oodm","ood Morning","ood Morning"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**goodmorning, {sender}! Have a great day. **")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        await message.reply_text(f"Goodnight, {sender}! Sleep tight.")


def get_random_sticker():
    stickers = [
        "CAACAgUAAxkBAAKM0GdMMkOGVmIanmjKcGOlOsd_7lXXAAJzCAACFYwYV5ZFOobqxjGMNgQ", # Sticker 1
        "CAACAgUAAxkBAAKMzWdMMg0xWeDDq3uUdq_fjhTOEarAAAJMDAACRgABIFdPOAqnvz9iMzYE", # Sticker 2
        "CAACAgUAAxkBAAKMymdMMebdkofgNNYU7Tzi-X0VKgLnAAI1BgACs2cYVma4ssyKE1ycNgQ", # Sticker 3
        "CAACAgUAAxkBAAKMxGdMMavNlAlju2_9sM15jrwRY3w6AAIhBgAC2YOAVQHB4kZyPtyrNgQ",
        "CAACAgUAAxkBAAKMx2dMMclFX1maKN30N0P__QwvH1kCAAJ5BAACtJhBVgAB3wW91RELhzYE",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "☀️",
        "🍿",
        "👻",
    ]
    return random.choice(emojis)

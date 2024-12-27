import re
from pyrogram import filters
import random
from AmritaXMusic import app

@app.on_message(filters.command(["gm", "goodmorning", "good morning"], prefixes=["/", "g", "G"]))
async def goodmorning_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    
    if send_sticker:
        sticker_id = get_random_sticker()
        await app.send_sticker(message.chat.id, sticker_id)  # Await the async call
        await message.reply_text(f"Good morning, {sender}! Have a wonderful day! ☀️")  # Await the async call
    else:
        emoji = get_random_emoji()
        await app.send_message(message.chat.id, emoji)  # Await the async call
        await message.reply_text(f"Good morning, {sender}! Have a wonderful day! {emoji}")  # Await the async call

def get_random_sticker():
    stickers = [
        "CAACAgUAAxkBAAKMxGdMMavNlAlju2_9sM15jrwRY3w6AAIhBgAC2YOAVQHB4kZyPtyrNgQ",  # Sticker 1
        "CAACAgUAAxkBAAKMx2dMMclFX1maKN30N0P__QwvH1kCAAJ5BAACtJhBVgAB3wW91RELhzYE",  # Sticker 2
        "CAACAgUAAxkBAAKMymdMMebdkofgNNYU7Tzi-X0VKgLnAAI1BgACs2cYVma4ssyKE1ycNgQ",  # Sticker 3
        "CAACAgUAAxkBAAKMzWdMMg0xWeDDq3uUdq_fjhTOEarAAAJMDAACRgABIFdPOAqnvz9iMzYE",
        "CAACAgUAAxkBAAKM0GdMMkOGVmIanmjKcGOlOsd_7lXXAAJzCAACFYwYV5ZFOobqxjGMNgQ",
    ]
    return random.choice(stickers)

def get_random_emoji():
    emojis = [
        "☀️",
        "🌞",
        "🌅",
    ]
    return random.choice(emojis)

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "26934275"
API_HASH = "bcf678e0b1a4ffd5f8e6d11f389fd428"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7966154925:AAGqnDq6o6V2QU6idJyZ2CSBwrp4h-ZzASc"
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","👿𝆺𝅥⃝𝐌ꝛ፝֟ ⚡️𝐋⃪⃬⃑𝛔⃪᪳᪰᪻𝛓⃪𝛂⃪𝐋⃪᪵ 𔑺 ⃪𝐊⃪᪵𝛊⃪𝛈⃪⃭⃐᪳᪼᪰𝐆⋆⏤͟͟͞𐏓⍣⃟🍷࿐﹡")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","@LoVeMuSic_HearTs_BoT")
# --------------------------------------------------------
BOT_NAME = getenv("🦋͢𝆺𝅥𓆩〭〬🤍 𝐋 ᴏ 𝐕 ᴇ 𝐇 ᴇ 𝐀 ʀ 𝐓 ᴢ 𝐌 ᴜ 𝐒 ɪ 𝐂🎙«🧘‍♂")
# ---------------------------13569561------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://ftyvfbgubhu7:hDZwwlNzlKBzls84@ameliamusicbot.f7dzw.mongodb.net/?retryWrites=true&w=majority&appName=AmeliaMusicbot"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 170000000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID",  --1002475141094))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = 6777334997


# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/crazyworld-izzy/144",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NS_TAMILCHAT_420")
SUPPORT_CHAT = getenv("SUPPORT_CHAT","https://t.me/NS_TAMILCHAT_420")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 555))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 904857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 9073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQFoY5UAHVlyd59olmssNSOA_qC22qPZl66zETVDJfHq_mmIyiD8SrTZLg9WiNu2Em4zP3kylG-qQmvzM_nQhucFGOYLCy5Hfa084ND302ltc8z3aI4zZaMCryTzeYOJyls6WgYVBouuwt8fKZySNFboL_qGyZyIugan066_fV2MtaEIC5fiOOTfUeMnvNWZXxfcO-SKaclopmoS1gW9mlBoXDg84u6-RhJ4aep3uhSipRDHCwD9_P1TdcQiN76QkOvulqm5EVe8hJWaDnmBbcaZqGAbvoHTuWX0fu0Xaqar3twiRqQaLM2L9Nkn2QVvZDGvLWDIqHjxoFeuTQL-FYdUvqs1fwAAAAF3M7q6AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/kCQ.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/k3F.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/k3F.jpg"
STATS_IMG_URL = "https://envs.sh/k3F.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

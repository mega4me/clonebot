#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6463722464:AAEW2t6PiG_InPs3AjLwlvOz1IqdL8oaXMw")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "21970953"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "914f964d0e1e15b1627b33e1d2ea35bd")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQFPQAkAb8opqzXFA7qtqXfvSAc8XCHG369xunogKtMNMiOVWvzDSaQMkr3mIScjGl7Bm8NlbXAb14ydXM_HA-RtLM3EdZLrQW0AUlgJgD7-pPyNq2sbvQPntTLv88zQj03cgvELsEptiFRVwqZZrYC-tuS20z4QpF3DD15tOHJowoeXxibzKAQ-VrCGlVfNV2CDU8Abruhh263HW8AQRJ_qEG-vd_OOwJEJXjFn9xkwDBtmN9vFwBLlH9A-VKJu9n2jFVXMrj_wPYIAaYam0QvavvGBjqFzrsdt3ypZ1efXjnn_8LZ_sXZvnIvsbuDV2mVvcMJFpEYrT7Xono5-LQdUnWfvRwAAAAF-AMX3AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://JohnWick:JohnWick@cluster0.ap7ydbx.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

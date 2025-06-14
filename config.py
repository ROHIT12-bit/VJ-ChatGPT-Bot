import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "20366634"))
API_HASH = environ.get("API_HASH", "72095ec36984aa9ceb0dbaa9cec31559")
BOT_TOKEN = environ.get("BOT_TOKEN", "7242758381:AAGkWrJ1z_0Jrmggh-Bo2D_6036Xj92NX4w")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002611038436"))
ADMINS = int(environ.get("ADMINS", "7845335174"))
DB_URI = environ.get("DB_URI", "mongodb+srv://rohitreddyathuru:R6Co7MOjTYQOAqcq@cluster0.xrwjpl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "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")
AI = is_enabled((environ.get("AI","True")), False)

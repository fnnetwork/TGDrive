from dotenv import load_dotenv
import os

# Load environment variables from the .env file, if present
load_dotenv()

# Telegram API credentials obtained from https://my.telegram.org/auth
API_ID = int(os.getenv("API_ID", "26481303"))  # Your Telegram API ID
API_HASH = os.getenv("API_HASH", "c950aa8fafd22287c3d4e9a344cb89ea")  # Your Telegram API Hash

# List of Telegram bot tokens used for file upload/download operations
BOT_TOKENS = os.getenv("BOT_TOKENS", "7820082001:AAGCzaBFVA47ckxy_wWnXYIqVP3Cl8HRvpk,7278268070:AAFyyAXKyxic_brEZr8s_cX3AZZJaH4itgs,7898076132:AAEF5F_8rPdQf-kBcbZP1dHpetifZ8BLAss")
BOT_TOKENS = BOT_TOKENS.strip(", ").split(",")
BOT_TOKENS = [token.strip() for token in BOT_TOKENS if token.strip()]

# List of Premium Telegram Account Pyrogram String Sessions used for file upload/download operations
STRING_SESSIONS = os.getenv("STRING_SESSIONS", "BAGUEpcAuPWmOQtHCDVsZFRlffAP9hkeR3k6TVaoxxdiBpUl1dz2Ntvm5l70DOKDYnpJXzIjPxfjk0GrtUBCNf74iFgmSWre1F7CXNQpUw-w8HmZI4EmScWgRheDytUMjejX6f7-LRQC_Ns_zksrhrLUDa2pj27wDdeRevtJC6pPvPnDqc3149eBGqaW26iirRBw4nT-kAbx-3EEwHcjp-WWFffEFdToSS5miEnNr-h8EA3ozWa6iH6_DLxyz288I_b6-ZE59l2YatLs415l5qHZlGQ83A3LGyRuxE1zKNll7jFfSJwWEdo_IE9oya3hUaSQE6aqR30aaON0-FNAqy_R7uwKvQAAAAHSItAjAA").strip(", ").split(",")
STRING_SESSIONS = [
    session.strip() for session in STRING_SESSIONS if session.strip() != ""
]

# Chat ID of the Telegram storage channel where files will be stored
STORAGE_CHANNEL = int(os.getenv("STORAGE_CHANNEL", "-1002394885619"))  # Your storage channel's chat ID

# Message ID of a file in the storage channel used for storing database backups
DATABASE_BACKUP_MSG_ID = int(
    os.getenv("DATABASE_BACKUP_MSG_ID", "2")
)  # Message ID for database backup

# Password used to access the website's admin panel
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "ELECTRA-TG-DRIVE-PRI")  # Default to "admin" if not set

# Determine the maximum file size (in bytes) allowed for uploading to Telegram
# 1.98 GB if no premium sessions are provided, otherwise 3.98 GB
if len(STRING_SESSIONS) == 0:
    MAX_FILE_SIZE = 1.98 * 1024 * 1024 * 1024  # 2 GB in bytes
else:
    MAX_FILE_SIZE = 3.98 * 1024 * 1024 * 1024  # 4 GB in bytes

# Database backup interval in seconds. Backups will be sent to the storage channel at this interval
DATABASE_BACKUP_TIME = int(
    os.getenv("DATABASE_BACKUP_TIME", 60)
)  # Default to 60 seconds

# Time delay in seconds before retrying after a Telegram API floodwait error
SLEEP_THRESHOLD = int(os.getenv("SLEEP_THRESHOLD", 60))  # Default to 60 seconds

# Domain to auto-ping and keep the website active
WEBSITE_URL = os.getenv("WEBSITE_URL", None)


# For Using TG Drive's Bot Mode

# Main Bot Token for TG Drive's Bot Mode
MAIN_BOT_TOKEN = os.getenv("MAIN_BOT_TOKEN", "7948986280:AAHZlxNXSN26imTu_SxfzWbDWnZKZEsIX5g")
if MAIN_BOT_TOKEN.strip() == "":
    MAIN_BOT_TOKEN = None

# List of Telegram User IDs who have admin access to the bot mode
TELEGRAM_ADMIN_IDS = os.getenv("TELEGRAM_ADMIN_IDS", "7593550190,7167145056").strip(", ").split(",")
TELEGRAM_ADMIN_IDS = [int(id) for id in TELEGRAM_ADMIN_IDS if id.strip() != ""]

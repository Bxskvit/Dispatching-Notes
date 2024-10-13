import os
from dotenv import load_dotenv  # getting bot token from dotenv

load_dotenv(dotenv_path="config\\.env")

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
DROPBOX_TOKEN = os.getenv('DROPBOX_TOKEN')
TEMPORARY_DATA_FOLDER = str(os.getenv('TEMPORARY_DATA_FOLDER'))
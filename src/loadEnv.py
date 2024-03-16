import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
SAVE_LOCATION = os.getenv('SAVE_LOCATION')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

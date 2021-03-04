import os
from dotenv import load_dotenv


load_dotenv()
PUSHOVER_API_URL = os.getenv("PUSHOVER_API_URL")
PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")
API_TOKEN = os.getenv("API_TOKEN")

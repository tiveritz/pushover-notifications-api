import os
import requests
import json
from dotenv import load_dotenv
from enum import Enum


class Priority(Enum):
    LOWEST = -2     # does not trigger any sound or vibration
    LOW = -1        # does not trigger sound or vibration but display alert
    NORMAL = 0      # triggers sound, vibration and display alert
    HIGH = 1        # triggers sound, vibration and display alert, bypass quiet hours
    EMERGENCY = 2   # same as high, but repeatedly alert until acknowledged

class PushoverNotification():
    def __init__(self, api_url, api_token, user_key):
        self.api_url = api_url
        self.api_token = api_token
        self.user_key = user_key
    
    def prepare_request(self, title, message, priority = Priority.NORMAL):
        self.title = title
        self.message = message
        self.priority = priority
        self.emergency_retry = 600    # 10 Munutes
        self.emergency_expire = 3600  # 1 Hour

    def post(self):
        payload = {
            'token' : self.api_token,
            'user' : self.user_key,
            'title' : self.title,
            'message' : self.message,
            'priority' : self.priority.value
        }

        if self.priority == Priority.EMERGENCY:
            payload['retry'] = self.emergency_retry
            payload['expire'] = self.emergency_expire

        r = requests.post(self.api_url, data = payload)
        self.status_code = r.status_code
        self.text = r.text


# Imports settings from the .env file
load_dotenv()
API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")
USER_KEY = os.getenv("USER_KEY")

# Sends the notification request to the API
r = PushoverNotification(API_URL, API_TOKEN, USER_KEY)
r.prepare_request("title", "message")
#r.prepare_request("title", "message", Priority.EMERGENCY)
r.post()

print(r.status_code)
print(r.text)

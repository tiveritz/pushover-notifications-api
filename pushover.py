import settings

from enum import Enum
import requests
import json


# Documentation: https://pushover.net/api

class Priority(Enum):
    LOWEST = -2     # does not trigger any sound or vibration
    LOW = -1        # does not trigger sound or vibration but display alert
    NORMAL = 0      # trigger sound, vibration and display alert
    HIGH = 1        # trigger sound, vibration and display alert, bypass quiet hours
    EMERGENCY = 2   # same as high, but repeatedly alert until acknowledged

class PushoverRequest():
    PUSHOVER_API_URL = settings.PUSHOVER_API_URL
    PUSHOVER_USER_KEY = settings.PUSHOVER_USER_KEY
    API_TOKEN = settings.API_TOKEN

    def __init__(self, title, message, priority = Priority.NORMAL):
        self.title = title
        self.message = message
        self.priority = priority
    
    def post(self):
        payload = {
            'token' : self.API_TOKEN,
            'user' : self.PUSHOVER_USER_KEY,
            'title' : self.title,
            'message' : self.message,
            'priority' : self.priority.value
        }

        if self.priority.value >= -2 and self.priority.value <= 1:

            r = requests.post(self.PUSHOVER_API_URL, data = payload)
            self.status_code = r.status_code
            self.text = r.text

        # emergency requires retry and expire and is not handled yet


r = PushoverRequest("title", "message")
r.post()

print(r.status_code)
print(r.text)

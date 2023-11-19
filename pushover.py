import requests
from enum import Enum


class Priority(Enum):
    LOWEST = -2    # does not trigger any sound or vibration
    LOW = -1       # does not trigger sound or vibration but display alert
    NORMAL = 0     # triggers sound, vibration and display alert
    HIGH = 1       # triggers sound, vibration and display alert, bypass quiet hours
    EMERGENCY = 2  # same as high, but repeatedly alert until acknowledged


class PushoverNotification:
    def __init__(self, api_url, api_token, user_key):
        self.api_url = api_url
        self.api_token = api_token
        self.user_key = user_key
        self.emergency_retry = 600    # 10 Minutes
        self.emergency_expire = 3600  # 1 Hour

    def notify(self, title, message, priority=Priority.NORMAL):
        payload = {
            'token': self.api_token,
            'user': self.user_key,
            'title': title,
            'message': message,
            'priority': priority.value
        }

        if priority == Priority.EMERGENCY:
            payload['retry'] = self.emergency_retry
            payload['expire'] = self.emergency_expire

        return requests.post(self.api_url, data=payload)

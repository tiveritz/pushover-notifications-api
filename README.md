# Pushover Real-Time Notifications
Pushover is a service to send and receive real-time notifications on
Android, iPhone, iPad, and Desktop (Android Wear and Apple Watch, too!)
It is very easy to use this service with the Pushover API.

API Documentation: [https://pushover.net/api](https://pushover.net/api)
<br />
<br />

## Usage
```
from pushover import PushoverNotification


API_URL = 'https://api.pushover.net/1/messages.json
API_TOKEN = # You will find this key on the device app you want to send the notifications to
USER_KEY = # Login with your Pushover Account, go to Dashboard https://pushover.net and create an Application/API Token

pushover = PushoverNotification(API_URL, API_TOKEN, USER_KEY)
response = pushover.notify('title', 'message')

print(response.status_code)
print(response.text)
```

You can set the Priority like:
```
from pushover import Priority
.
.
.
r.prepare_request('title', 'message', Priority.EMERGENCY)
```

Available Priorities
```
LOWEST = -2     # does not trigger any sound or vibration
LOW = -1        # does not trigger sound or vibration but display alert
NORMAL = 0      # triggers sound, vibration and display alert
HIGH = 1        # triggers sound, vibration and display alert, bypass quiet hours
EMERGENCY = 2   # same as high, but repeatedly alert until acknowledged
```
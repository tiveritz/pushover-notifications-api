## Executing
Pushover is a service to send and receive real-time notifications on
Android, iPhone, iPad, and Desktop (Android Wear and Apple Watch, too!)
It is very easy to use this service with the Pushover API.
<br /><br />

API Documentation: [https://pushover.net/api](https://pushover.net/api)

#### Requirenments
python-dotenv==0.15.0\
requests==2.25.1

#### Environment Variables
Include the following environment variables into your .env file
  * PUSHOVER_API_URL=https://api.pushover.net/1/messages.json
  * PUSHOVER_USER_KEY -> You will find this key on the device app you want
to send the notifications to
  * API_TOKEN -> Login with your Pushover Account, go to Dashboard
  https://pushover.net and create an Application/API Token
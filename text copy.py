
import random, schedule, time

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

GOOD_MORNING_QUOTES = [
    "Good morning!",
    "Hey, how are you"
    
    ]

def send_message(quotes_list=GOOD_MORNING_QUOTES):

    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )

    quote = GOOD_MORNING_QUOTES[random.randint(0, len(GOOD_MORNING_QUOTES))]
    schedule.every().day.at("10:30").do(send_message,GOOD_MORNING_QUOTES,quote)
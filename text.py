import random, schedule
from twilio.rest import Client
 


INSPIRATIONAL_QUOTES = [

    "On a deeper level you are already complete. When you realize that, there is a playful, joyous energy behind what you do.",
    "Most people are about as happy as they make up their minds to be.",
    "Be happy for this moment, this moment is your life.",
    "The secret of happiness is not in doing what one likes, but in liking what one does.",
    "The simplest things can bring the most happiness.",
    "Trust your own instincts, go inside, follow your heart. Right from the start. Go ahead and stand up for what you believe in. As I’ve learned, that’s the path to happiness.",
    "We tend to forget that happiness doesn’t come as a result of getting something we don’t have, but rather of recognizing and appreciating what we do have."


]

# def send_message(
quotes_list=INSPIRATIONAL_QUOTES

account = "ACf6c0cdfc33ce0d5a476c85d0126c6df8"
token = "51a6307405bcb87f2f68e7ea1679785f"
client = Client(account, token)
quote = quotes_list[random.randint(0, len(quotes_list)-1)]
# client.messages.create(to="+17733325792",
#                            from_=+16082003114,
#                            body=quote
#                            )

# client.messages.create(to="+17738697713",
#                            from_=+16082003114,
#                            body=quote
#                            )

client.messages.create(to="+16083462744",
                           from_=+16082003114,
                           body=quote
                           )

# send a message in the morning
# schedule.every().day.at("08:00").do(send_message, INSPIRATIONAL_QUOTES)

# Testing
# schedule.every().day.at("15:56").do(send_message, INSPIRATIONAL_QUOTES)



# while True:
#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(2)

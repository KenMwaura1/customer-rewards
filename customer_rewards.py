import africastalking as at
from dotenv import load_dotenv
import os

from customer_search import CustomerQuery

load_dotenv()
# get the environment values from the .env file
at_username = os.getenv('at_username')
at_api_key = os.getenv('at_api_key')
# Set phone_number in international format
phone_number = os.getenv('phone_number')

at.initialize(at_username, at_api_key)
airtime = at.Airtime
account = at.Application

print(account.fetch_application_data())
# print(CustomerQuery.customer_query()[1])

def send_airtime():
    # Set The 3-Letter ISO currency code and the amount
    amount = "5"
    currency_code = "KES"

    try:
        # That's it hit send and we'll take care of the rest
        responses = airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
        print(responses)
    except Exception as e:
        print("Encountered an error while sending airtime:%s" % str(e))


send_airtime()

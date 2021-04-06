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


def send_airtime():
    # Set The 3-Letter ISO currency code and the amount
    amount = "5"
    currency_code = "KES"
    numbers = []
    for n in CustomerQuery.customer_query():
        print(n[1], n[2], n[-1])
        numbers.append(n[-1])
    print(numbers)
    for number in numbers:
        try:
            response = airtime.send(phone_number=number, amount=amount, currency_code=currency_code)
            print(response)
        except Exception as e:
            print(f"Encountered an error while sending airtime. More error details below\n {e}")


send_airtime()

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# params = {
#     'term': 'food',
#     'lang': 'en'
# }

# response = client.search('Copenhagen', **params)

# for business in response.businesses:
#     print(business.name)

# Create function that takes in a term and location and print top businesses

# term = input("What food are you looking for?")
# location = input("Where do you want to eat?")


def get_businesses(term, location):
    auth = Oauth1Authenticator(
    consumer_key=os.environ["CONSUMER_KEY"],
    consumer_secret=os.environ["CONSUMER_SECRET"],
    token=os.environ["TOKEN"],
    token_secret=os.environ["TOKEN_SECRET"]
    )

    client = Client(auth)
    params = {
        'term': term,
        'lang': 'en',
            }
    response = client.search(location, **params)

    businesses = []

    for business in response.businesses:
        businesses.append({"name": business.name, 
        "rating": business.rating, 
        "phone": business.phone
        })
    
    return businesses[:3]

    # term = input("What food are you looking for?")
    # location = input("Where do you want to eat?")
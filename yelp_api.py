# test change git commit

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

auth = Oauth1Authenticator(
  consumer_key=os.environ['CONSUMER_KEY'],
  consumer_secret=os.environ['CONSUMER_SECRET'],
  token=os.environ['TOKEN'],
  token_secret=os.environ['TOKEN_SECRET']
)

client = Client(auth)

# term = 'food'
# lang = 'en'
# location = 'Southlake, TX'


def get_restaurant(term, location, lang):
  consumer_key = os.environ['CONSUMER_KEY']
  consumer_secret=os.environ['CONSUMER_SECRET']
  params = {
    'term': term,
    'lang': lang,
    'limit': 3,
    'sort': 2
  } 

  response = client.search(location, **params)

  restaurants = []

  for business in response.businesses:
    print(business.name, business.rating, business.review_count, business.phone)
    restaurants.append({"name":business.name,
       "rating":business.rating,
        "review_count":business.review_count})


  return restaurants

# restaurants = get_restaurant(term, location, lang)

# print(restaurants)
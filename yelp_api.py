# this is a pain in the ass to get working

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

def get_businesses(city, term): 
	params = {
	'city': city,
	'term': term,
	'lang': 'en',
	'limit': 3
	}

	client = Client(auth)

	response = client.search(city, term **params)

	businesses = []

	for business in response.businesses:
		businesses.append({"name": business.name,
			"rating": business.rating,
			"whereabouts": business.location.address,
			"phone": business.phone
		})

	return businesses

# businesses = get_businesses('city', 'term')

# print(businesses)
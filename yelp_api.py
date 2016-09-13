from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term): 
	auth = Oauth1Authenticator(
    	consumer_key=os.environ['CONSUMER_KEY'],
    	consumer_secret=os.environ['CONSUMER_SECRET'],
    	token=os.environ['TOKEN'],
    	token_secret=os.environ['TOKEN_SECRET']
	)

	client = Client(auth)

	params = {
    	'term': term,
    	'lang': 'en',
    	'limit': 4
	}

	response = client.search(location, **params)

	businesses = []

	for business in response.businesses:
		businesses.append({"name": business.name,
			"rating": business.rating,
			"whereabouts": business.location.address,
			"phone": business.phone
		})

	return businesses

# businesses = get_businesses('location', 'term')

# print(businesses)
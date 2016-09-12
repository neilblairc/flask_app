from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

def get_businesses(term): 
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
    	'limit': 3
	}

	response = client.search(location, **params)

	businesses = []

	for business in response.businesses:
		businesses.append({"Name": business.name,
			"Word on the street": business.snippet_text,
			"Random score": business.rating,
			"Hipster votes": business.review_count,
			"Whereabouts": business.location.address,
			"Phone": business.phone
		})

	return businesses

# businesses = get_businesses('San Francisco', 'cobbler')

# print(businesses)
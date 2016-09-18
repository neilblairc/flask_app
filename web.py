from flask import Flask, render_template, request
from yelp_api import get_businesses
import os
app = Flask(__name__)

@app.route("/")
def index():
	location = request.values.get('location')
	term = request.values.get('term')
	lang = 'en'
	if location:
		restaurant = yelp_api.get_restaurant(term, location, lang)
	else:
		restaurant = None
	return render_template('index.html', restaurant=restaurant)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
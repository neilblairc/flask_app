from flask import Flask, render_template, request
from yelp_api import get_businesses
import os
app = Flask(__name__)

@app.route("/")
def index():
	term = None
	businesses = None
	location = None
	if(request.values.get('topic'))!=None:
		term = request.values.get('topic')
		city = request.values.get('location')
		businesses = yelp_search(term, location)
		return render_template('index.html', searchresult=businesses)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, jsonify, render_template, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
import scrapemars
import pandas as pd


# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = MongoClient("mongodb://localhost:27017/mars_app")
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrapes():
    mars = mongo.db.mars
    mars_data = scrapemars.webscrape()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=True)




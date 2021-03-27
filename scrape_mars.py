
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)

    mars_info = {}
    mars_info['latest_title'] = news_title
    mars_info['latest_p'] = news_p
    mars_info['hemispheres'] = all_hemisphere_image_urls
    #mars_info['mars_facts'] = html_table
    marsdata.append(mars_info)  


    if__name__ == "__main__":
        app.run(debug=True)




# Route to render index.html template using data from Mongo
    # Create our session (link) from Python to the DB
    #session = Session(engine)
    # collect scraping result from jupyter notebook and return python dictionary containing all scraped data
    #marsdata = {}
    #mars_info['latest_title'] = news_title
   # mars_info['latest_p'] = news_p
   # mars_info['featured_image'] = featured_image_url
   # mars_info['hemispheres'] = all_hemisphere_image_urls
    #mars_info['mars_facts'] = html_table

    # marsdata.append(mars_info)        
    #Close session
   # session.close()

    #return jsonify(marsdata)


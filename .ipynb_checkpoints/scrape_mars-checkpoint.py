{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import Dependencies\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import time\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from flask import Flask, render_template\n",
    "import pymongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# setup mongo connection\n",
    "conn = \"mongodb://localhost:27017\"\n",
    "client = pymongo.MongoClient(conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# connect to mongo db and collection\n",
    "db = client.mars_db\n",
    "mars_col = db.mars_collection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def scrape_info():\n",
    "    # Set up Splinter\n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "    \n",
    "    # Visit NASA Mars News Site\n",
    "    url = 'https://mars.nasa.gov/news/'\n",
    "    browser.visit(url)\n",
    "    \n",
    "     # Scrape page into Soup\n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "    \n",
    "    # Get title\n",
    "    news_title= soup.find_all(\"div\", class_=\"content_title\")\n",
    "    news_title[1].text\n",
    "    \n",
    "    # Return results of paragraph text\n",
    "    news_p= soup.find_all(\"div\", class_=\"article_teaser_body\")\n",
    "    news_p[0].text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " # Visit jpl Mars Site\n",
    "    images_url= \"https://spaceimages-mars.com/\"\n",
    "    browser.visit(images_url)\n",
    "    \n",
    "    # featured_image_url =\n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "    \n",
    "    jpl=soup.find(\"a\", class_=\"showimg fancybox-thumbs\")['href']\n",
    "    featured_image_url=images_url+jpl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit page and use pandas to scrape table\n",
    "spacefacts=pd.read_html(\"https://space-facts.com/mars\")\n",
    "df=spacefacts[0]\n",
    "\n",
    "html_table= df.to_html(index=False, header=False)\n",
    "# clean up the data by removing unwanted new lines\n",
    "html_table= html_table.replace('\\n', '')\n",
    "\n",
    "# save the table directly to a file\n",
    "df.to_html('table.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " # Visit NASA Mars News Site\n",
    "    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "    browser.visit(url)\n",
    "    \n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "    \n",
    "    all_hemisphere_image_urls = []\n",
    "\n",
    "# Start by getting a list of all of the hemispheres via links\n",
    "links = browser.find_by_css(\"a.product-item h3\")\n",
    "\n",
    "# Next, loop through all the links and click.\n",
    "# Find the sample anchor and return the href\n",
    "for x in range(len(links)):\n",
    "    hemisphere = {}\n",
    "    \n",
    "    # find the elements on each loop \n",
    "    browser.find_by_css(\"a.product-item h3\")[x].click()\n",
    "    \n",
    "    # Next, we find the Sample image anchor tag and extract the first href\n",
    "     # Access the href attribute with bracket notation\n",
    "    sample_elemt = browser.links.find_by_text('Sample').first\n",
    "    hemisphere['img_url'] = sample_elemt['href']\n",
    "    \n",
    "    # Get Hemisphere title\n",
    "    hemisphere['title'] = browser.find_by_css(\"h2.title\").text\n",
    "    \n",
    "    # Append the dictionary with the image url string and the hemisphere title to a list\n",
    "    all_hemisphere_image_urls.append(hemisphere)\n",
    "    \n",
    "    # Navigate backwards and output results\n",
    "    browser.back()\n",
    "all_hemisphere_image_urls\n",
    "\n",
    " # Close the browser after scraping\n",
    "    browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

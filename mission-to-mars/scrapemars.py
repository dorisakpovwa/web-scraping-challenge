#!/usr/bin/env python
# coding: utf-8

# Mission to Mars

# In[1]:


#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import pandas as pd
import pymongo
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

def webscrape():

# In[3]:


# Visit NASA Mars News Site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # time.sleep(1)


    # In[4]:


    # Scrape page into Soup object
    html = browser.html
    soup = bs(html, "html.parser")


    # In[5]:


    # Get title
    news_title= soup.find_all("div", class_="content_title")
    news_title= news_title[1].text
    news_title


    # In[6]:


    # Return results of paragraph text
    news_p= soup.find_all("div", class_="article_teaser_body")
    news_p= news_p[0].text
    news_p


    # In[7]:


    # create dictionary for title and paragrapgh
    mars_info = {}
    mars_info['latest_title'] = news_title
    mars_info['latest_p'] = news_p
    mars_info


    # JPL Mars Space Images- Featured Image

    # In[8]:



    # images_url= "https://www.jpl.nasa.gov/images?search=&category=Mars"
    # browser.visit(images_url)


    # In[9]:


    # images_data=browser.find_by_text("FULL IMAGE")
    # images_data.click()


    # In[10]:


    #a1=browser.is_element_present_by_text("more info", wait_time=1)
    #element2_is=browser.links.find_by_partial_text("more info")
    #element2_is.click()


    # In[11]:


    images_url= "https://spaceimages-mars.com/"
    browser.visit(images_url)


    # In[12]:


    # featured_image_url =
    html = browser.html
    soup = bs(html, "html.parser")
    #display(soup)


    # In[13]:


    # Make sure to find the image url to the full size.jpg image
    # save complete url string for this image
    jpl=soup.find("a", class_="showimg fancybox-thumbs")['href']
    featured_image_url=images_url+jpl
    featured_image_url
    #The given url was not working. I got this url from my tutor


    # Mars Facts

    # In[14]:


    # Visit page and use pandas to scrape table
    # Get facts about the planet including Diameter, Mass etc
    spacefacts=pd.read_html("https://space-facts.com/mars")
    df=spacefacts[0]
    df


    # In[15]:


    # Use pandas to convert data to a HTML table string
    # html_table = df_to_html()
    html_table= df.to_html(index=False, header=False)
    html_table


    # In[16]:


    # clean up the data by removing unwanted new lines
    html_table= html_table.replace('\n', '')
    html_table


    # In[17]:


    # save the table directly to a file
    df.to_html('table.html')


    # In[18]:


    #open to view the file in a browser
    #!start table.html


    # Mars Hemispheres

    # In[19]:


    # Visit the USGS Astrogeology site
    # Obtain high resolution images for each of Mar's hemispheres
    # url of initial page to be scraped
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # In[20]:


    # grab html page and create soup object
    html = browser.html
    soup = bs(html, "html.parser")
    #display(soup)


    # In[21]:


    # save both image url string for the full resolution hemisphere image and title containing name 
    # store in python dictionary using keys img_url and title
    # initialize variables to store information
    all_hemisphere_image_urls = []

    # Start by getting a list of all of the hemispheres via links
    links = browser.find_by_css("a.product-item h3")

    # Next, loop through all the links and click.
    # Find the sample anchor and return the href
    for x in range(len(links)):
        hemisphere = {}
        
        # find the elements on each loop 
        browser.find_by_css("a.product-item h3")[x].click()
        
        # Get Hemisphere title
        hemisphere['title'] = browser.find_by_css("h2.title").text
        # Next, find the Sample image anchor tag and extract the first href
        # Access the href attribute with bracket notation
        
        sample_elemt = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elemt['href']
        
        # Append the dictionary with the image url string and the hemisphere title to a list
        all_hemisphere_image_urls.append(hemisphere)
        
        # Navigate backwards and output results
        browser.back()
    all_hemisphere_image_urls


    # In[22]:


    # create dictionary for all scraped data
    mars_infos = {}
    mars_infos['latest_title'] = news_title
    mars_infos['latest_p'] = news_p
    mars_infos['featured_image'] = featured_image_url
    mars_infos['hemispheres'] = all_hemisphere_image_urls
    mars_infos['mars_facts'] = html_table
    return mars_infos


    # In[23]:



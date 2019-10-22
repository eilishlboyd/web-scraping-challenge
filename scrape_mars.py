#!/usr/bin/env python
# coding: utf-8

# In[97]:


#Imports & Dependencies
get_ipython().system('pip install selenium')
get_ipython().system('pip install splinter')
from splinter import Browser
from bs4 import BeautifulSoup
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[98]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[99]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[100]:


article = soup.find("div", class_="list_text")
news_p = article.find("div", class_="article_teaser_body").text
news_title = article.find("div", class_="content_title").text
news_date = article.find("div", class_="list_date").text
print(news_date)
print(news_title)
print(news_p)


# In[106]:


url2 = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url2)

# Scrape the browser into soup and use soup to find the image of mars
# Save the image url to a variable called `img_url`
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
image = soup.find("img", class_="thumb")["src"]
img_url = "https://jpl.nasa.gov"+image
featured_image_url = img_url
# Use the requests library to download and save the image from the `img_url` above
import requests
import shutil
response = requests.get(img_url, stream=True)
with open('img.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
    
# Display the image with IPython.display
from IPython.display import Image
Image(url='img.jpg')


# In[107]:


import tweepy
# Twitter API Keys
from key_vault import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
target_user = "marswxreport"
full_tweet = api.user_timeline(target_user , count = 1)
mars_weather=full_tweet[0]['text']
mars_weather


# In[108]:


url3 = "http://space-facts.com/mars/"
browser.visit(url3)


# In[109]:


import pandas as pd
facts_url = "https://space-facts.com/mars/"
browser.visit(facts_url)
mars_data = pd.read_html(facts_url)
mars_data = pd.DataFrame(mars_data[0])
mars_facts = mars_data.to_html(header = False, index = False)
print(mars_facts)


# In[110]:


url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url4)


# In[111]:


import time 
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
mars_hemis=[]


# In[112]:


for i in range (4):
    time.sleep(5)
    images = browser.find_by_tag('h3')
    images[i].click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    partial = soup.find("img", class_="wide-image")["src"]
    img_title = soup.find("h2",class_="title").text
    img_url = 'https://astrogeology.usgs.gov'+ partial
    dictionary={"title":img_title,"img_url":img_url}
    mars_hemis.append(dictionary)
    browser.back()


# In[113]:


print(mars_hemis)


# In[ ]:





# In[ ]:





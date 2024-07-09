#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install beautifulsoup4


# In[5]:


pip install selenium


# In[11]:


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

l=[]
o={}

PATH = '/Applications/chromedriver'

# Set up the Selenium WebDriver
service = Service(executable_path=PATH)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the home page
driver.get("https://www.myntra.com/sweatshirts/h%26m/hm-men-black-regular-fit-cotton-sweatshirt/20305162/buy")

html_content = driver.page_source

soup=BeautifulSoup(html_content,'html.parser')


try:
    o["title"]=soup.find('h1',{'class':'pdp-title'}).text.lstrip().rstrip()
except:
    o["title"]=None

try:
    o["rating"]=soup.find('div',{'class':'index-overallRating'}).find('div').text.lstrip().rstrip()
except:
    o["rating"]=None

try:
    o["price"]=soup.find('span',{'class':'pdp-price'}).text.lstrip().rstrip()
except:
    o["price"]=None


l.append(o)


print(l)


# Close the browser
driver.quit()


# In[ ]:





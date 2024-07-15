#!/usr/bin/env python
# coding: utf-8

# In[4]:


# pip install beautifulsoup4
# pip3 install beautifulsoup4


# In[5]:


# pip install selenium
# pip3 install selenium


# In[11]:


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Initialize an empty list to store product details
l=[]

# Initialize an empty dictionary to store a single product's details
o={}

# Path to the ChromeDriver executable
PATH = '/Applications/chromedriver'

# Set up the Selenium WebDriver
service = Service(executable_path=PATH)
options = webdriver.ChromeOptions()
# Uncomment the next line to run the browser in headless mode
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the home page
driver.get("https://www.myntra.com/sweatshirts/h%26m/hm-men-black-regular-fit-cotton-sweatshirt/20305162/buy")

# Get the page source HTML content
html_content = driver.page_source

# Parse the HTML content using BeautifulSoup
soup=BeautifulSoup(html_content,'html.parser')


# Try to extract the product title and store it in the dictionary
try:
    o["title"]=soup.find('h1',{'class':'pdp-title'}).text.lstrip().rstrip()
except:
    o["title"]=None

# Try to extract the product rating and store it in the dictionary
try:
    o["rating"]=soup.find('div',{'class':'index-overallRating'}).find('div').text.lstrip().rstrip()
except:
    o["rating"]=None

# Try to extract the product price and store it in the dictionary
try:
    o["price"]=soup.find('span',{'class':'pdp-price'}).text.lstrip().rstrip()
except:
    o["price"]=None


# Append the dictionary to the list
l.append(o)

# Print the list containing the product details
print(l)


# Close the browser
driver.quit()


# In[ ]:





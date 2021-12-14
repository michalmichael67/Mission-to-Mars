#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[6]:
slide_elem.find('div', class_='content_title')


# In[7]:
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[14]:
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[15]:
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[16]:
html = browser.html
img_soup = soup(html, 'html.parser')


# In[17]:
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[18]:
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[20]:
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[21]:
df.to_html()


# In[22]:
browser.quit()




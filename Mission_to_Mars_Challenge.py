#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[25]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[26]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[27]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[28]:


slide_elem.find('div', class_='content_title')


# In[29]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[30]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[31]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[32]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[33]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[34]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[35]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[36]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[37]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[38]:


df.to_html()


# ## D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[91]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[92]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

hemisphere_html = browser.html
hemisphere_soup = soup(hemisphere_html, 'html.parser')

items = hemisphere_soup.find_all('div', class_='item')

for item in items:
    hemispheres = {}
    # click on each hemisphere link
    rel_url = item.find('a', class_='itemLink product-item')['href']
    browser.visit(url + rel_url)
    
    #set up ability to parse hemisphere link
    html = browser.html
    html_soup = soup(html,'html.parser')
    
    #retrieve title
    hemisphere_title = html_soup.find('h2', class_='title').text
    
    #navigate full resolution image url
    hemisphere_img_url = html_soup.find('img', class_='wide-image').get('src')
    
    hemispheres['img_url'] = f'{url}{hemisphere_img_url}'
    hemispheres['title'] = hemisphere_title
    hemisphere_image_urls.append(hemispheres)
    
    # Browse back to repeat
    browser.back()
    


# In[93]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[94]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





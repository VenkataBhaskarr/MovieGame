#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


import requests
from bs4 import BeautifulSoup


# In[6]:


url = 'https://www.imdb.com/search/title/?title_type=feature&year=2020-01-01,2020-12-31&languages=te&start=1&explore=languages&ref_=adv_nxt'
url2 = 'https://www.imdb.com/search/title/?title_type=feature&year=2020-01-01,2020-12-31&languages=te&start=51&explore=languages&ref_=adv_nxt'
url3 = 'https://www.imdb.com/search/title/?title_type=feature&year=2020-01-01,2020-12-31&languages=te&start=101&explore=languages&ref_=adv_nxt'


# In[7]:


response = requests.get(url)
response2 = requests.get(url2)
response3 = requests.get(url3)

    


# In[8]:


soup = BeautifulSoup(response.content, "html.parser")
soup2 = BeautifulSoup(response2.content, "html.parser")
soup3 = BeautifulSoup(response3.content, "html.parser")


# In[9]:


movie_name = []


# In[10]:


movie_data = soup.findAll('div' , attrs = {'class' : 'lister-item mode-advanced'})
movie_data2 = soup2.findAll('div' , attrs = {'class' : 'lister-item mode-advanced'})
movie_data3 = soup3.findAll('div' , attrs = {'class' : 'lister-item mode-advanced'})


# In[11]:


for movie in movie_data:
    movie_name.append(movie.h3.a.text)
for movie in movie_data2:
    movie_name.append(movie.h3.a.text)
for movie in movie_data3:
    movie_name.append(movie.h3.a.text)    


# In[26]:


for movie in movie_data:
    actors.append(movie.find_all('div' , class_ = 'lister-item-content').p)


# In[24]:


print(actors)


# In[46]:


actors = []


# In[39]:


actor_data = soup.findAll('div' , attrs = {'class' : 'lister-item-content'})
actor_data2 = soup2.findAll('div' , attrs = {'class' : 'lister-item-content'})
actor_data3 = soup3.findAll('div' , attrs = {'class' : 'lister-item-content'})


# In[47]:


for actor in actor_data:
    hero = actor.find('p' , class_ = '').findAll('a')
    actors.append(hero[1].text)

   


# In[48]:


print(actors)


# In[57]:


for actor in actor_data2:
    zero = actor.find('p', class_ = '').findAll('a')
    actors.append(zero[1].text)


# In[56]:


print(actors)


# In[ ]:


df = pd.dataframe()


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import quandl


# In[2]:


mydata_01 = quandl.get('FRED/GDP')


# In[3]:


mydata_01


# In[16]:


import pandas as pd


# In[8]:


mydata_01.to_csv('C:/Users/neri_/Downloads/Python for Finance - Notebook Files/example_01.csv')


# In[9]:


mydata_01


# In[34]:


mydata_02 = pd.read_excel('C:/Users/neri_/Downloads/Python for Finance - Notebook Files/57 Importing Data - Part III/CSV/Python 3 CSV/Data_03.xlsx')


# In[35]:


mydata_02


# In[ ]:





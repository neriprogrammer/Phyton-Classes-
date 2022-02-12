#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plit


# In[5]:


MSFT = wb.DataReader('MSFT', data_source='yahoo', start='2000-1-1')


# In[6]:


MSFT.head()


# In[7]:


MSFT.tail()


# In[8]:


MSFT['simple_return'] = (MSFT['Adj Close'] / MSFT['Adj Close'].shift(1)) - 1
print(MSFT['simple_return'])


# In[9]:


#Taxa simples de retorno 

MSFT['simple_return'] = (MSFT['Adj Close'] / MSFT['Adj Close'].shift(1)) - 1
print(MSFT['simple_return'])


# In[10]:


TSLA = wb.DataReader('TSLA', data_source='yahoo', start='2019-1-1')


# In[11]:


TSLA


# In[15]:


TSLA['simple_return'] = (TSLA['Adj Close'] / TSLA['Adj Close'].shift(1)) - 1
print(TSLA['simple_return'])


# In[17]:


TSLA.tail()


# In[37]:


TSLA['simple_return'].plot(figsize=(8,5))


# In[24]:


avg_returns_d = TSLA['simple_return'].mean()
avg_returns_d


# In[25]:


avg_returns_a = TSLA['simple_return'].mean() * 250
avg_returns_a


# In[35]:


print (str(round(avg_returns_a,5) * 100)+ ' %') 


# In[38]:


MSFT['simple_return'].plot(figsize=(8,5))


# In[40]:


#Taxa Logaritmica de retorno
FB = wb.DataReader('FB', data_source='yahoo', start='2015-1-1')


# In[41]:


FB


# In[43]:


FB['log_return'] = np.log(FB['Adj Close'] / FB['Adj Close'].shift(1))
print (FB['log_return'])


# In[45]:


FB['log_return'].plot(figsize=(8,5))


# In[47]:


log_return_d = FB['log_return'].mean()
log_return_d


# In[52]:


log_return_a = FB['log_return'].mean() * 250
log_return_a


# In[53]:


print (str(round(log_return_d, 5) *100) + '%')


# In[ ]:





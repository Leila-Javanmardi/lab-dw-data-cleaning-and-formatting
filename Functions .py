#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
data=pd.read_csv('https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv')
import numpy as np
import re


# In[25]:


def cleaning_data_general (data: pd.DataFrame):
    #general cleaning for column names 
    
    data2=data.copy()
    data2.columns=data2.columns.str.lower().str.strip().str.replace(' ','_')
    data2.rename(columns ={'st':'state'}, inplace = True)
    # dropping rows where all the values are null
    data2 = data2.dropna(how = 'all')
    data2= data2.drop_duplicates()
     
    return data2


data_cleaned=cleaning_data_general(data)
data_cleaned.head(4)


# In[16]:





# In[27]:


def cleaning_gender(df: pd.DataFrame):
    
    data2 = df.copy()     # copy of original data to be on the safe side!
    gender_mapping = {'M':0, 'F':1,'Femal':1,'Male':0,'female':1,}
    data2['gender']=data2['gender'].map(gender_mapping)
    #replace Nan with 2
    data2['gender'] = data2['gender'].fillna(2)
    # cast the value integer
    data2['gender'] = data2['gender'].astype(int)
    return data2

data_cleaned=cleaning_gender(data_cleaned)
data_cleaned.head(4)


# In[ ]:





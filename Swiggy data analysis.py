#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df=pd.read_csv(r"C:\Users\user\Downloads\archive (4).zip")


# In[6]:


df.head(7)


# In[7]:


df.shape


# In[8]:


df.info()


# In[9]:


df.drop(['Rating','Offer','URL'],axis=1,inplace=True)


# In[10]:


df.shape


# In[11]:


df.drop_duplicates(inplace=True)
df.shape


# # Cleaning the dataset column wise
# 

# In[12]:


df.rename(columns={'Cost for Two (in Rupees)':'Costfor2'},inplace=True)


# In[13]:


df.head()


# In[15]:


resttype=df['Restaurant Name'].value_counts(ascending=False)
resttype


# In[16]:


restlessthan5=resttype[resttype<5]
def handle_rtype(value):
    if(value in restlessthan5):
        return 'others'
    else:
        return value
df['Restuarant Name']=df['Restaurant Name'].apply(handle_rtype)
df['Restuarant Name'].value_counts()


# In[19]:


df['Category'].nunique()


# In[20]:


category=df['Category'].value_counts(ascending=False)
category


# In[21]:


categorylessthan100= category[category<100]


# In[22]:


def handle_category(value):
    if(value in categorylessthan100):
        return 'others'
    else:
        return value
        
df['Category'] = df['Category'].apply(handle_category)
df['Category'].value_counts()


# # Plotting graphs

# In[37]:


plt.figure(figsize = (13,10))
ax = sns.countplot(data = df, x = 'Area')

for bars in ax.containers:
    ax.bar_label(bars)

plt.title('No. of restaurants area wise')
plt.ylabel('count of restaurants')
plt.xticks(rotation=90)


# In[47]:


df1= df['Category'].value_counts()
df2=df1.iloc[1:]
df2


# In[48]:


df2.to_csv('category_type')
df3 = pd.read_csv('category_type')
df3.columns=["Category","count"]
df3


# In[53]:


plt.figure(figsize = (13,10))
sns.barplot(data=df3,x='Category',y='count')
plt.xticks(rotation=30)

plt.title('No. of restaurants category wise')

#plt.xticks(rotation=90)


# In[ ]:





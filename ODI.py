#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_excel("C://Users//ISHAN//OneDrive//Desktop//sachin//archive 2//Sachin Tendulkar Batting Stats.xlsx")
df


# ## Extracting ODI Data 

# In[3]:


df1=df[df["Match Type"]=="ODI"]


# In[4]:


df1


# In[5]:


df.isnull().sum()


# In[6]:


df1.Runs.unique()


# In[7]:


df2=df1[(df1.Runs!="DNB")&(df1.Runs!="TDNB")]
df2.isnull().sum()
df2.drop(["Mins"],axis=1,inplace=True)
df2


# In[8]:


df2.isnull().sum()


# In[9]:


pd.to_numeric(df2.Runs)
df2.Runs.unique()


# ### Total Runs in ODI 

# In[10]:


df2.Runs.sum()


# ### Total number of 4 

# In[11]:


df2["4s"].sum()


# ### Total numbers of 6s

# In[12]:


df2["6s"].sum()


# ### Count of Dismissals 

# In[13]:


df2.Dismissal.value_counts()


# ### Names of team which got Sachin out at 0 score 

# In[14]:


df2[df2.Runs==0].shape


# In[15]:


filtered_df2=df2[df2.Runs==0]
filtered_df2.Opposition.value_counts()


# ### Avg Strike Rate 

# In[16]:


df2.SR.mean()


# ### Max Strike Rate 

# In[17]:


df2.SR.max()


# ### Min Strike Rate

# In[18]:


df2.SR.min()


# ### Max Score against which Team

# In[19]:


df2.Runs.max()


# In[20]:


max_score=df2.Runs.max()
max_scor_df2=df2[df2.Runs==max_score]
max_scor_df2.Opposition


# ### Numbers of centuries in ODI

# In[21]:


df2[df2.Runs>=100].shape


# In[22]:


centuries_df2=df2[df2.Runs>=100]


# In[23]:


centuries_df2.Opposition.value_counts()


# In[24]:


centuries_df2.pivot_table(index="Opposition",values="SR",aggfunc=["mean","max","min"])


# ### Number of Fifties

# In[25]:


df2[(df2.Runs>=50)&(df2.Runs<=99)].shape


# In[26]:


fifties_df2=df2[(df2.Runs>=50)&(df2.Runs<=99)]
fifties_df2.Opposition.value_counts()


# ### Converting Fifties into Century 

# In[27]:


conversion_df2=df2[(df2.Runs>=50)&(df2.Runs>=100)]
conversion_df2.shape


# In[28]:


conversion_df2.Opposition.value_counts()


# ### Count of matches India won/lost when Sachin scored 100 

# In[29]:


df2[(df2.Result=="Won")&(df2.Runs>=100)].shape


# In[30]:


df2[(df2.Result=="Lost")&(df2.Runs>=100)].shape


# ### Matches against Australia

# In[31]:


df2[df2.Opposition=="Australia"].shape


# In[32]:


df2[(df2.Result=="Won")&(df2.Opposition=="Australia")].shape


# In[33]:


df2[(df2.Result=="Won")&(df2.Opposition=="Australia")&(df2.Runs>=100)].shape


# In[34]:


df2[(df2.Result=="Lost")&(df2.Opposition=="Australia")&(df2.Runs>=100)].shape


# ### Matches against Bangladesh 

# In[35]:


df2[df2.Opposition=="Bangladesh"].shape


# In[36]:


df2[(df2.Result=="Won")&(df2.Opposition=="Bangladesh")].shape


# In[37]:


df2[(df2.Result=="Won")&(df2.Opposition=="Bangladesh")&(df2.Runs>=100)].shape


# In[38]:


df2[(df2.Result=="Lost")&(df2.Opposition=="Bangladesh")&(df2.Runs>=100)].shape


# ### Matches against New Zealand

# In[39]:


df2[df2.Opposition=="New Zealand"].shape


# In[40]:


df2[(df2.Result=="Won")&(df2.Opposition=="New Zealand")].shape


# In[41]:


df2[(df2.Result=="Won")&(df2.Opposition=="New Zealand")&(df2.Runs>=100)].shape


# In[42]:


df2[(df2.Result=="Lost")&(df2.Opposition=="New Zealand")&(df2.Runs>=100)].shape


# ### Matches against Sri Lanka 

# In[43]:


df2[df2.Opposition=="Sri Lanka"].shape


# In[44]:


df2[(df2.Result=="Won")&(df2.Opposition=="Sri Lanka")].shape


# In[45]:


df2[(df2.Result=="Won")&(df2.Opposition=="Sri Lanka")&(df2.Runs>=100)].shape


# In[46]:


df2[(df2.Result=="Lost")&(df2.Opposition=="Sri Lanka")&(df2.Runs>=100)].shape


# ### Matches against Pakistan

# In[47]:


df2[df2.Opposition=="Pakistan"].shape


# In[48]:


df2[(df2.Result=="Won")&(df2.Opposition=="Pakistan")].shape


# In[49]:


df2[(df2.Result=="Won")&(df2.Opposition=="Pakistan")&(df2.Runs>=100)].shape


# In[50]:


df2[(df2.Result=="Lost")&(df2.Opposition=="Pakistan")&(df2.Runs>=100)].shape


# ### Matches against South Africa

# In[51]:


df2[df2.Opposition=="South Africa"].shape


# In[52]:


df2[(df2.Result=="Won")&(df2.Opposition=="South Africa")].shape


# In[53]:


df2[(df2.Result=="Won")&(df2.Opposition=="South Africa")&(df2.Runs>=100)].shape


# In[54]:


df2[(df2.Result=="Lost")&(df2.Opposition=="South Africa")&(df2.Runs>=100)].shape


# ### Matches against Zimbabwe

# In[55]:


df2[df2.Opposition=="Zimbabwe"].shape


# In[56]:


df2[(df2.Result=="Won")&(df2.Opposition=="Zimbabwe")].shape


# In[57]:


df2[(df2.Result=="Won")&(df2.Opposition=="Zimbabwe")&(df2.Runs>=100)].shape


# In[58]:


df2[(df2.Result=="Lost")&(df2.Opposition=="Zimbabwe")&(df2.Runs>=100)].shape


# ### Matches against Kenya

# In[59]:


df2[df2.Opposition=="Kenya"].shape


# In[60]:


df2[(df2.Result=="Won")&(df2.Opposition=="Kenya")].shape


# In[61]:


df2[(df2.Result=="Won")&(df2.Opposition=="Kenya")&(df2.Runs>=100)].shape


# In[62]:


df2[(df2.Result=="Lost")&(df2.Opposition=="Kenya")&(df2.Runs>=100)].shape


# ### Matches against West Indies

# In[63]:


df2[df2.Opposition=="West Indies"].shape


# In[64]:


df2[(df2.Result=="Won")&(df2.Opposition=="West Indies")].shape


# In[65]:


df2[(df2.Result=="Won")&(df2.Opposition=="West Indies")&(df2.Runs>=100)].shape


# In[66]:


df2[(df2.Result=="Lost")&(df2.Opposition=="West Indies")&(df2.Runs>=100)].shape


# ### Matches against Namibia

# In[67]:


df2[df2.Opposition=="Namibia"].shape


# In[68]:


df2[(df2.Result=="Won")&(df2.Opposition=="Namibia")].shape


# In[69]:


df2[(df2.Result=="Won")&(df2.Opposition=="Namibia")&(df2.Runs>=100)].shape


# In[70]:


df2[(df2.Result=="Lost")&(df2.Opposition=="Namibia")&(df2.Runs>=100)].shape


# ### Matches against England

# In[71]:


df2[df2.Opposition=="England"].shape


# In[72]:


df2[(df2.Result=="Won")&(df2.Opposition=="England")].shape


# In[73]:


df2[(df2.Result=="Won")&(df2.Opposition=="England")&(df2.Runs>=100)].shape


# In[74]:


df2[(df2.Result=="Lost")&(df2.Opposition=="England")&(df2.Runs>=100)].shape


# ### Extracting Date from the data 
# 

# In[75]:


df2['Start Date'] = pd.to_datetime(df2['Start Date'])


# In[76]:


df2['year']=df2["Start Date"].dt.year


# In[77]:


a=df2.year.unique()


# In[78]:


df2["Count"]=np.where(df2.Runs>=100,1,0)


# ### Count of centuries in a year

# In[79]:


df3=df2.pivot_table(index="year",values="Count",aggfunc="sum")
df3


# In[80]:


b=df3.Count.to_list()


# ### Plotting graph of YEAR v/s COUNT OF CENTURIES

# In[81]:


fig = plt.figure(figsize=(20, 6))
plt.title("YEAR v/s NO. OF CENTURIES")
plt.xlabel("YEARS")
plt.ylabel("NO. OF CENTURIES")
plt.xticks(a)
plt.grid()

plt.bar(a,b)


# ### AVG Strike Rate by a year

# In[82]:


df4=df2.pivot_table(index="year",values="SR",aggfunc="mean")
df4


# In[83]:


c=df4.SR.to_list()


# ### Plotting a graph YEAR v/s AVG STRIKE RATE

# In[84]:


fig = plt.figure(figsize=(20, 6))
plt.title("YEAR v/s AVG STRIKE RATE")
plt.xlabel("YEARS")
plt.ylabel("AVG STRIKE RATE")
plt.xticks(a)
plt.grid()

plt.plot(a,c)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sb


# In[2]:


df=pd.read_excel("C://Users//ISHAN//OneDrive//Desktop//sachin//archive 2//Sachin Tendulkar Batting Stats.xlsx")
df


# In[3]:


df1=df[df["Match Type"]=="Test"]
df1


# In[4]:


df1.isnull().sum()


# In[ ]:





# In[5]:


df1.isnull().sum()
df1.Runs.unique()


# In[6]:


df2=df1[(df1.Runs!="DNB")&(df1.Runs!="TDNB")]
df2.isnull().sum()
df2.drop(["Mins"],axis=1,inplace=True)
df2


# In[7]:


df2.isnull().sum()


# In[8]:


df3=df2.fillna(0)


# In[9]:


df4=df3.drop(['BF'], axis=1)


# In[10]:


df4.isnull().sum()


# In[11]:


df4.Runs.unique()


# In[12]:


df4.iloc[330,0] = "13"


# In[13]:


df4.Runs.unique()


# ### Total Runs 

# In[14]:


df4.Runs=pd.to_numeric(df4["Runs"])


# In[15]:


df4.Runs.sum()


# ### Total numbers of 4s

# In[16]:


df4["4s"].sum()


# ### Total numbers of 6s

# In[17]:


df4["6s"].sum()


# ### Count of Dismissals

# In[18]:


df4.Dismissal.value_counts()


# In[19]:


df4.Dismissal.replace("not out","Not Out",inplace=True)
df4.Dismissal.replace("caught","Caught",inplace=True)
df4.Dismissal.replace("run out","Run Out",inplace=True)
df4.Dismissal.replace("lbw","LBW",inplace=True)
df4.Dismissal.replace("bowled","Bowled",inplace=True)


# In[20]:


df4.Dismissal.value_counts()


# ### Nams of teams which got Sachin out at 0

# In[21]:


df4[df4.Runs==0].shape


# In[22]:


out_at_0=df4[df4.Runs==0]


# In[23]:


out_at_0.Opposition.value_counts()


# ### Avg Strike Rate

# In[24]:


df4.SR.mean()


# ### Max Strike Rate

# In[25]:


df4.SR.max()


# ### Min Strike Rate
# 

# In[26]:


df4.SR.min()


# ### Maximum runs scored against which team

# In[27]:


df4.Runs.max()


# In[28]:


max_score=df4.Runs.max()
max_scor_df=df4[df4.Runs==max_score]
max_scor_df.Opposition


# ### Numbers of centuries scored in Test
# 

# In[29]:


df4[df4.Runs>=100].shape


# In[30]:


centuries_scored_df=df4[df4.Runs>=100]


# In[31]:


centuries_scored_df.Opposition.value_counts()


# ### Strike Rate while hitting a century

# In[32]:


centuries_scored_df.pivot_table(index="Opposition",values="SR",aggfunc=["mean","max","min"])


# ### Number of fiftes 

# In[33]:


df4[(df4.Runs>=50)&(df4.Runs<=99)].shape



# In[34]:


fifties_df=df4[(df4.Runs>=50)&(df4.Runs<=99)]
fifties_df.Opposition.value_counts()


# ### Converting fifties into century

# In[35]:


df4[(df4.Runs>=50)&(df4.Runs<=100)].shape


# In[36]:


converting_df=df4[(df4.Runs>=50)&(df4.Runs<=100)]
converting_df.Opposition.value_counts()


# ### Count of matches India won/lost when Sachin scored 100 

# In[37]:


df4[(df4.Runs>=100)&(df4.Result=="Won")].shape


# In[38]:


df4[(df4.Runs>=100)&(df4.Result=="Loss")].shape


# ### Matches against Australia

# In[39]:


df4[df4.Opposition=="Australia"].shape


# In[40]:


df4[(df4.Opposition=="Australia")&(df4.Result=="Won")].shape


# In[41]:


df4[(df4.Opposition=="Australia")&(df4.Result=="Won")&(df4.Runs>=100)].shape


# In[42]:


df4[(df4.Opposition=="Australia")&(df4.Result=="Loss")&(df4.Runs>=100)].shape


# ### Matches against Bangladesh

# In[43]:


df4[df4.Opposition=="Bangladesh"].shape


# In[44]:


df4[(df4.Opposition=="Bangladesh")&(df4.Result=="Won")].shape


# In[45]:


df4[(df4.Opposition=="Bangladesh")&(df4.Result=="Won")&(df4.Runs>=100)].shape


# In[46]:


df4[(df4.Opposition=="Australia")&(df4.Result=="Loss")&(df4.Runs>=100)].shape


# ### Matches against England

# In[47]:


df4[df4.Opposition=="England"].shape


# In[48]:


df4[(df4.Opposition=="England")&(df4.Result=="Won")].shape


# In[49]:


df4[(df4.Opposition=="England")&(df4.Result=="Won")&(df4.Runs>=100)].shape


# In[50]:


df4[(df4.Opposition=="England")&(df4.Result=="Loss")&(df4.Runs>=100)].shape


# ### Matches against New Zealand

# In[51]:


df4[df4.Opposition=="New Zealand"].shape


# In[52]:


df4[(df4.Opposition=="New Zealand")&(df4.Result=="Won")].shape


# In[53]:


df4[(df4.Opposition=="New Zealand")&(df4.Result=="Won")&(df4.Runs>=100)].shape


# In[54]:


df4[(df4.Opposition=="New Zealand")&(df4.Result=="Loss")&(df4.Runs>=100)].shape


# ### Matches against Pakistan 

# In[55]:


df4[df4.Opposition=="Pakistan"].shape


# In[56]:


df4[(df4.Opposition=="Pakistan")&(df4.Result=="Won")].shape


# In[57]:


df4[(df4.Opposition=="Pakistan")&(df4.Result=="Won")&(df4.Runs>=100)].shape


# In[58]:


df4[(df4.Opposition=="Pakistan")&(df4.Result=="Loss")&(df4.Runs>=100)].shape


# ### Matches agianst South Africa

# In[59]:


df4[df4.Opposition=="South Africa"].shape


# In[60]:


df4[(df4.Opposition=="South Africa")&(df4.Result=="Won")].shape


# In[61]:


df4[(df4.Opposition=="South Africa")&(df4.Result=="Won")&(df4.Runs>=100)].shape


# In[62]:


df4[(df4.Opposition=="South Africa")&(df4.Result=="Loss")&(df4.Runs>=100)].shape


# ### Matches against Sri Lanka

# In[63]:


df4[df4.Opposition=="Sri Lanka"].shape


# In[64]:


df4[(df4.Opposition=="Sri Lanka")&(df4.Result=="Won")].shape


# In[65]:


df4[(df4.Opposition=="Sri Lanka")&(df4.Result=="Won")&(df4.Runs>=100)].shape


# In[66]:


df4[(df4.Opposition=="Sri Lanka")&(df4.Result=="Loss")&(df4.Runs>=100)].shape


# ### Matches against West Indies

# In[67]:


df4[df4.Opposition=="West Indies"].shape


# In[68]:


df4[(df4.Opposition=="West Indies")&(df4.Result=="Won")].shape


# In[69]:


df4[(df4.Opposition=="West Indies")&(df4.Result=="Won")&(df4.Runs>=100)].shape


# In[70]:


df4[(df4.Opposition=="West Indies")&(df4.Result=="Loss")&(df4.Runs>=100)].shape


# ### Matches against Zimbabwe

# In[71]:


df4[df4.Opposition=="Zimbabwe"].shape


# In[72]:


df4[(df4.Opposition=="Zimbabwe")&(df4.Result=="Won")].shape


# In[73]:


df4[(df4.Opposition=="Zimbabwe")&(df4.Result=="Won")&(df4.Runs>=100)].shape


# In[74]:


df4[(df4.Opposition=="Zimbabwe")&(df4.Result=="Loss")&(df4.Runs>=100)].shape


# ### Extracting Date from the data

# In[75]:


df4["Date"]=pd.to_datetime(df4["Start Date"])
df4["Year"]=df4["Start Date"].dt.year
df4


# ### Counting number of centuries in a year

# In[76]:


df4["Count"]=np.where(df4.Runs>=100,1,0)
df4.head(20)


# In[79]:


df5=df4.pivot_table(index="Year",values="Count",aggfunc="sum")
df5


# In[78]:


a=df4.Year.unique()
a


# In[81]:


b=df5.Count.to_list()
b


# ### Plotting graph of YEAR v/s COUNT OF CENTURIES

# In[85]:


fig = plt.figure(figsize=(20, 6))
plt.title("YEAR v/s NO. OF CENTURIES")
plt.xlabel("YEARS")
plt.ylabel("NO. OF CENTURIES")
plt.xticks(a)
plt.grid()

plt.bar(a,b)


# In[87]:


df6= df4.pivot_table(index="Year",values="SR",aggfunc="mean")
df6


# In[94]:


c=df6.SR.to_list()
a.sort()
a


# ### Plotting a graph YEAR v/s AVG STRIKE RATE

# In[95]:


fig = plt.figure(figsize=(20, 6))
plt.title("YEAR v/s AVG STRIKE RATE")
plt.xlabel("YEARS")
plt.ylabel("AVG STRIKE RATE")
plt.xticks(a)
plt.grid()

plt.plot(a,c)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # 100 Centuries 
# 

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# ### Importing Data of the 100 Centuries

# In[2]:


df=pd.read_csv("C://Users//ISHAN//OneDrive//Desktop//sachin//archive//Sachin Tendulkar - 100 Centuries.csv")


# In[3]:


df


# ### Counting NULL Values

# In[4]:


df.isnull().sum()


# ### Cleaning Data By Changing The NULL Values

# In[5]:


df=df.drop("Test ",axis=1)
df=df.fillna({"Strike Rate":df["Strike Rate"].mean() })


# ### Counting NULL Values

# In[6]:


df.isnull().sum()


# ### Maximum Score while hitting a century 

# In[7]:


max_score=df.Score.max()
max_score_df=df[df.Score==max_score]
print("The max score is ",max_score)
print(max_score_df.Against)


# ### Checking Datatypes

# In[8]:


df.dtypes


# ### Average Strike Rate while hitting a century 

# In[9]:


print("The avg strike rate is ", df["Strike Rate"].mean())


# ### Min Strike Rate while hitting a century 

# In[10]:


print("The min strike rate is ",df['Strike Rate'].min())


# ### Max Strike Rate while hitting a century 

# In[11]:


print("The max strike rate is ",df['Strike Rate'].max())


# ### Against which team Sachin scored century with Max Strike Rate

# In[12]:


max_strike_rate_value = df['Strike Rate'].max()
filtered_df = df[df['Strike Rate'] == max_strike_rate_value]

print("The max strike rate is against :",filtered_df.Against)


# ### Against which team Sachin scored century with Min Strike Rate

# In[13]:


min_strike_rate_value = df['Strike Rate'].min()
filtered_df1 = df[df['Strike Rate'] == min_strike_rate_value]
filtered_df1.Against


# ### Count of centuries sachin scored against each team 

# In[14]:


df.Against.value_counts()


# ### Avg,Min,Max Strike rate again each team while hitting a century 

# In[15]:


df.pivot_table(index="Against",values="Strike Rate",aggfunc=["mean","max","min"])


# ### No. of matches India won,lost,drawn when sachin hitted a century 

# In[16]:


df.Result.value_counts()


# ### No. of matches India won when Sachin is captain & also he scored a century 

# In[17]:


df[(df.Captain=="Yes") & (df.Result=="Won")].shape


# ### No. of matches India lost when Sachin is captain & also he scored a century 

# In[18]:


df[(df.Captain=="Yes") & (df.Result=="Lost")].shape


# ### No. of matches drawn when Sachin is captain & also he scored a century 

# In[19]:


df[(df.Captain=="Yes") & (df.Result=="Drawn")].shape


# ### No. of matches India won when Sachin is not a captain & also he scored a century 

# In[20]:


df[(df.Captain=="No") & (df.Result=="Won")].shape


# ### No. of matches Drawn when Sachin is not a captain & also he scored a century 

# In[21]:


df[(df.Captain=="No") & (df.Result=="Drawn")].shape


# ### No. of matches India Lost when Sachin is not a captain & also he scored a century 

# In[22]:


df[(df.Captain=="No") & (df.Result=="Lost")].shape


# ### No. of matches India won against Australia when Sachin hitted a century 

# In[23]:


df[(df.Against=="Australia")& (df.Result=="Won")].shape


# ### No. of matches India lost against Australia when Sachin hitted a century 

# In[24]:


df[(df.Against=="Australia")& (df.Result=="Lost")].shape


# ### No. of matches India drawn against Australia when Sachin hitted a century 

# In[25]:


df[(df.Against=="Australia")& (df.Result=="Drawn")].shape


# ### No. of matches India won against Bangladesh when Sachin hitted a century 

# In[26]:


df[(df.Against=="Bangladesh")& (df.Result=="Won")].shape


# ### No. of matches India lost against Bangladesh when Sachin hitted a century 

# In[27]:


df[(df.Against=="Bangladesh")& (df.Result=="Lost")].shape


# ### No. of matches India drawn against Bangladesh when Sachin hitted a century 

# In[28]:


df[(df.Against=="Bangladesh")& (df.Result=="Drawn")].shape


# ### No. of matches India won against England when Sachin hitted a century 

# In[29]:


df[(df.Against=="England")& (df.Result=="Won")].shape


# ### No. of matches India lost against England when Sachin hitted a century 

# In[30]:


df[(df.Against=="England")& (df.Result=="Lost")].shape


# ### No. of matches drawn against England when Sachin hitted a century 

# In[31]:


df[(df.Against=="England")& (df.Result=="Drawn")].shape


# ### No. of matches India won against Kenya when Sachin hitted a century 

# In[32]:


df[(df.Against=="Kenya")& (df.Result=="Won")].shape


# ### No. of matches India lost against Kenya when Sachin hitted a century 

# In[33]:


df[(df.Against=="Kenya")& (df.Result=="Lost")].shape


# ### No. of matches drawn against Kenya when Sachin hitted a century 

# In[34]:


df[(df.Against=="Kenya")& (df.Result=="Drawn")].shape


# ### No. of matches India won against Namibia when Sachin hitted a century 

# In[35]:


df[(df.Against=="Namibia")& (df.Result=="Won")].shape


# ### No. of matches India lost against Namibia when Sachin hitted a century 

# In[36]:


df[(df.Against=="Namibia")& (df.Result=="Lost")].shape


# ### No. of matches drawn against Namibia when Sachin hitted a century 

# In[37]:


df[(df.Against=="Namibia")& (df.Result=="Drawn")].shape


# ### No. of matches India won against New Zealand when Sachin hitted a century 

# In[38]:


df[(df.Against=="New Zealand")& (df.Result=="Won")].shape


# ### No. of matches India lost against Namibia when Sachin hitted a century 

# In[39]:


df[(df.Against=="New Zealand")& (df.Result=="Lost")].shape


# ### No. of matches drawn against Namibia when Sachin hitted a century 

# In[40]:


df[(df.Against=="New Zealand")& (df.Result=="Drawn")].shape


# ### No. of matches India won against Pakistan when Sachin hitted a century 

# In[41]:


df[(df.Against=="Pakistan")& (df.Result=="Won")].shape


# ### No. of matches India lost against Pakistan when Sachin hitted a century 

# In[42]:


df[(df.Against=="Pakistan")& (df.Result=="Lost")].shape


# ### No. of matches drawn against Pakistan when Sachin hitted a century 

# In[43]:


df[(df.Against=="Pakistan")& (df.Result=="Drawn")].shape


# ### No. of matches India won against South Africa when Sachin hitted a century 

# In[44]:


df[(df.Against=="South Africa")& (df.Result=="Won")].shape


# ### No. of matches India lost against South Africa when Sachin hitted a century 

# In[45]:


df[(df.Against=="South Africa")& (df.Result=="Lost")].shape


# ### No. of matches drawn against South Africa when Sachin hitted a century 

# In[46]:


df[(df.Against=="South Africa")& (df.Result=="Drawn")].shape


# ### No. of matches India won against Sri Lanka when Sachin hitted a century 

# In[47]:


df[(df.Against=="Sri Lanka")& (df.Result=="Won")].shape


# ### No. of matches India lost against Sri Lanka when Sachin hitted a century 

# In[48]:


df[(df.Against=="Sri Lanka")& (df.Result=="Lost")].shape


# ### No. of matches drawn against Sri Lanka when Sachin hitted a century 

# In[49]:


df[(df.Against=="Sri Lanka")& (df.Result=="Drawn")].shape


# ### No. of matches India won against West Indies when Sachin hitted a century 

# In[50]:


df[(df.Against=="West Indies")& (df.Result=="Won")].shape


# ### No. of matches India lost against West Indies when Sachin hitted a century 

# In[51]:


df[(df.Against=="West Indies")& (df.Result=="Lost")].shape


# ### No. of matches drawn against West Indies when Sachin hitted a century 

# In[52]:


df[(df.Against=="West Indies")& (df.Result=="Drawn")].shape


# ### No. of matches India won against Zimbabwe when Sachin hitted a century 

# In[53]:


df[(df.Against=="Zimbabwe")& (df.Result=="Won")].shape


# ### No. of matches India lost against Zimbabwe when Sachin hitted a century 

# In[54]:


df[(df.Against=="Zimbabwe")& (df.Result=="Lost")].shape


# ### No. of matches drawn against Zimbabwe when Sachin hitted a century 

# In[55]:


df[(df.Against=="Zimbabwe")& (df.Result=="Drawn")].shape


# In[56]:


df_result =df[(df.Result=="N/R")]
df_result


# In[57]:


df_result1 =df[(df.Result=="Tied")]
df_result1


# ### Count of Player of the match award when he hitted a century 

# In[58]:


df["Player of the match"].value_counts()


# ### Count of centuries at a particular venue

# In[59]:


df.Venue.value_counts()


# ### Extracting year from the Date coloumn

# In[60]:


df['Date'] = pd.to_datetime(df['Date '])


# In[61]:


df['year']=df.Date.dt.year


# In[62]:


df


# ### Count of centuries in a year

# In[63]:


df4=df.pivot_table(index="year",values="Score",aggfunc="count")
df4.rename(columns={'Score': 'No. of Centuries'}, inplace=True)
df4


# In[64]:


a=df4["No. of Centuries"].to_list()
b=df.year.unique()
b


# ### Plotting graph of Year v/s Count of centuries

# In[65]:


fig = plt.figure(figsize=(20, 6))
plt.title("YEAR v/s NO. OF CENTURIES")
plt.xlabel("YEARS")
plt.ylabel("NO. OF CENTURIES")
plt.xticks(b)
plt.grid()

plt.bar(b,a)


# ### Avg Strike Rate in a year 

# In[66]:


df5=df.pivot_table(index="year",values="Strike Rate",aggfunc="mean")
df5.rename(columns={"Strike Rate":"Avg Strike Rate"},inplace=True)
df5


# In[67]:


c=df.year.unique()
d=df5["Avg Strike Rate"].to_list()


# ### Plotting graph of Year v/s Avg Strike Rate 

# In[68]:


fig = plt.figure(figsize=(20, 6))
plt.title("YEAR v/s AVG STRIKE RATE")
plt.xlabel("YEARS")
plt.ylabel("AVG STRIKE RATE")
plt.xticks(c)
plt.grid()

plt.plot(c,d)


# In[ ]:





# In[ ]:





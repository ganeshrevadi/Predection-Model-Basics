#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello world")


# In[2]:


#Create a data frame
raw_data = {'first _name':['Sam','Ziva','Kia','Robin'],'degree':['phd','MBA','M tech','B tech'], 'age':[25,34,43,34]}
import pandas as pd
df = pd.DataFrame(raw_data)
print(df)


# In[ ]:


df.to_csv(r"Example.csv")


# In[3]:


df.to_csv(r"Example.csv")


# In[4]:


df=pd.read_csv("Example.csv")
print(df)


# In[5]:


df.head()


# In[6]:


df.head(2)


# In[7]:


del df['Unnamed: 0']


# In[8]:


df


# In[9]:


df.describe()


# In[10]:


import numpy as np
d = {'A':[1,2,np.NaN],'B':[1,np.Nan,np.NaN]}
df = pd.DataFrame(d)
df


# In[11]:


import numpy as np
d = {'A':[1,2,np.NaN],'B':[1,np.NaN,np.NaN]}
df = pd.DataFrame(d)
df


# In[12]:


df1= df.dropna()
df1


# In[14]:


newdf=df.fillna('Ab')
newdf


# In[1]:


import pandas as pd
df=pd.DataFrame({'one':[20,10,1000,20,40],'two':[2000,20,90,3,9]})
print(df)
print(df.replace({1000:10,2000:20}))


# In[2]:


mylist=[[1,2,3],[4,5,6],[7,8,9]]
mylist


# In[3]:


import numpy as np
ar1=np.array(mylist)
ar1


# In[4]:


a1=np.random.rand(5)
a1


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd



# In[20]:


titanic = pd.read_csv(r"C:\Users\hp\Desktop\titanic.csv")


# In[21]:


titanic


# In[22]:


titanic.head(10)


# In[23]:


titanic.tail(3)


# In[24]:


titanic.describe()


# In[25]:


max(titanic)


# In[26]:


min(titanic)


# In[16]:


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
x = 900 + np.random.normal(0,600,8)
y = 900 + np.random.normal(0,600,8)

plt.scatter(x,y) #التمثيل بالنقاط
plt.title('scatter plot')
plt.xlabel('x column')
plt.ylabel('y column')
plt.show()


# In[30]:


import matplotlib.pyplot as plt

#DATA FOR LINE 1 
x1= np.array([0, 1, 2, 3, 4, 5])
y1= np.array([0, 65, 988, 45, 10, 91])

#DATA FOR LINE 2
x2= np.array([0, 1, 2, 3, 4, 5])
y2= np.array([700, 20, 654, 20, 39, 70])


#CREATING SUBPLOTS
fig, axs = plt.subplots(2, 2)

#PLOTTING LINE 1 
axs[0, 0].plot(x1, y1)
axs[0, 0].set_title('line1')

#PLOTTING LINE 2
axs[0, 1].plot(x2, y2)
axs[0, 1].set_title('line2')


# In[ ]:





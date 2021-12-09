#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas
import statistics 
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
col_names=['x','y']
dp=pandas.read_csv("Food-Truck-LineReg.csv",names=col_names)
print(dp)
x=dp['x'].values
y=dp['y'].values
sx=statistics.stdev(x)
print("SD OF X:",sx)
sy=statistics.stdev(y)
print("SD OF Y:",sy)
mx=statistics.mean(x)
print("MEAN OF X:",mx)
my=statistics.mean(y)
print("MEAN OF Y:",my)
corr, _ = pearsonr(x, y)
print("CORRELATION:",corr)
m=corr*sy/sx
print("SLOPE:",m)
c=my-m*mx
print("INTERCET:",c)
pred_y=(m*x)+c
print(pred_y)
plt.scatter(x, y,color="g")
plt.plot(x,pred_y)
plt.show()


# In[52]:


#cost
cost=y-pred_y
print("COST:",cost)


# In[47]:


#SSE
sq=(y-pred_y)**2
sse=sum(sq)
print("SSE:",sse)


# In[49]:


#SSR
sq1=(pred_y-my)**2
ssr=sum(sq1)
print("SSE:",ssr)


# In[50]:


#SST
sq2=(y-my)**2
sst=sum(sq2)
print("SST:",sst)


# In[51]:


#R^2
r=ssr/sst
print("R^2:",r)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[11]:


def normalization(l):
    maxnum=max(l)
    minnum=min(l)
    for i in range(0,len(l)):
        l[i]=(l[i]-minnum)/(maxnum-minnum)
    sum=0
    for n in l:
        sum+=n
    mean=sum/len(l)
    print("Mean after Normalizing:",mean)
    
l=[78,65,56,87,91,37,49,77,62,59,95,63,42,55,72,68,81,39,45,49]
normalization(l)


# In[10]:


l=[1,2,3,4,5]
x=min(l)
print(x)


# In[35]:


from sklearn.preprocessing import Normalizer
l=[[4,1,2,2],[1,3,9,3],[5,7,5,1]]
print(Normalizer().fit_transform(l))
print(Normalizer().fit_transform(l).mean())
print(Normalizer().fit_transform(l).std())


# In[34]:


from sklearn.preprocessing import StandardScaler
data = [[0, 0], [0, 0], [1, 1], [1, 1]]
print(StandardScaler().fit_transform(data))
print(StandardScaler().fit_transform(data).mean(axis=0))
print(StandardScaler().fit_transform(data).std())


# In[30]:


import statistics as st
def standardization(l):
    dev=st.stdev(l)
    mean=st.mean(l)
    for i in range(0,len(l)):
        l[i]=(l[i]-mean)/dev
    print(st.mean(l))
    print(st.stdev(l))
    
l=[1,5,3,7,6]
standardization(l)


# In[ ]:





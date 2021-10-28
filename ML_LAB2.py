#!/usr/bin/env python
# coding: utf-8

# In[49]:


def find(arr):
    sum=0
    arr.sort()
    for i in arr:
        sum+=i
    mean=sum/len(arr)
    if len(arr)%2==0:
        median=arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)]
    else:
        median=arr[int(len(arr)/2)]
    f=[0]*max(arr)
    for ele in arr:
        f[ele-1]+=1
    mode=f.index(max(f))+1
    print("Mean:",mean,"\nMedian:",median,"\nMode:",mode)
    
arr=[1,2,3,5,5,5,3,3,5]
find(arr)


# In[45]:


def findbuiltin(arr):
    mean=st.mean(arr)
    median=st.median(arr)
    mode=st.mode(arr)
    print("Mean:",mean,"\nMedian:",median,"\nMode:",mode)
    
arr=[1,2,3,5,5,5,3,3,5]
import statistics as st
findbuiltin(arr)


# In[60]:


def vandsd(l):
    sum=0
    j=0
    for i in l:
        j+=i
    mean=j/len(l)
    for ele in l:
        sum+=pow((mean-ele),2)
    variance=sum/(len(l)-1)
    sd=os.sqrt(variance)
    print("Variance:",variance,"\nStandard Deviation:",sd)
    
l=[46,69,32,60,52,41]
import math as os
vandsd(l)


# In[63]:


def varsd(l):
     print("Variance:",st.variance(l),"\nStandard Deviation:",st.stdev(l))
        

l=[46,69,32,60,52,41]
varsd(l)


# In[ ]:





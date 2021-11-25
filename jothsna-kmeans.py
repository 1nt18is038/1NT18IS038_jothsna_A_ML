#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas
import math 
dp=pandas.read_csv("datapoints.csv")
dp['x1'] = dp['x1'].astype(float)
dp['x2'] = dp['x2'].astype(float)
k=2
index=0
flag=True
cen=pandas.read_csv("datapoints.csv",nrows=k)
print(cen)
cen['x1'] = cen['x1'].astype(float)
cen['x2'] = cen['x2'].astype(float)
oldp=[ [0]*2 for i in range(k)]
for i in range(k):
    oldp[i][0]=cen['x1'][i]
    oldp[i][1]=cen['x2'][i]
print(oldp)
while(flag):
    for i in range(k):
        cen['x1'][i]=oldp[i][0]
        cen['x2'][i]=oldp[i][1]
    m1=[0]*len(dp)
    p=[ [0]*2 for i in range(k)]
    print(p)
    size=[0]*k
    for i in range(len(dp)):
        l=[]
        for j in range(len(cen)):
            s1=pow((dp['x1'][i]-cen['x1'][j]),2)
            s2=pow((dp['x2'][i]-cen['x2'][j]),2)
            s=math.sqrt(s1+s2)
            l.append(s)
        index=l.index(min(l))
        p[index][0]+=dp['x1'][i]
        p[index][1]+=dp['x2'][i]
        print(p)
        size[index]+=1
    for i in range(k):
        p[i][0]=p[i][0]/size[i]
        p[i][1]=p[i][1]/size[i]
    print(p)
    print(oldp)
    print("\n")from sklearn.cluster import kmeans
dp=pandas.read_csv("datapoints.csv")
KM=kmeans(n_clusters=2)
KM.fit(dp)
print(KM.cluster_centers_)
    count=0
    for i in range(k):
        for j in range(2):
            if(p[i][j]==oldp[i][j]):
                count+=1
    if(count==k*2):
        flag=False
    for i in range(k):
        oldp[i][0]=p[i][0]
        oldp[i][1]=p[i][1]


# In[5]:


import pandas
from sklearn.cluster import KMeans
dp=pandas.read_csv("datapoints.csv")
KM=KMeans(n_clusters=2)
KM.fit(dp)
print(KM.cluster_centers_)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





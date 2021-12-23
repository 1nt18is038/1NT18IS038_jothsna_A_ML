#!/usr/bin/env python
# coding: utf-8

# In[152]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

col_names=['x1','x2','result']
ds=pd.read_csv('Student-University.csv',header=None,names=col_names)

# input
x = ds.iloc[:, [0, 1]].values
  
# output
y = ds.iloc[:, 2].values

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.20, random_state = 0)
print(ytrain)


# In[153]:


import numpy as np
x1=xtrain[:,0]
x2=xtrain[:,1]
b0=0.0
b1=0.0
b2=0.0
print(ytrain)
epoch=10000
alpha=0.001
while(epoch>0):
    for i in range(len(xtrain)):
        prediction=1/(1+np.exp(-(b0+b1*x1[i]+b2*x2[i])))
        b0=b0+alpha*(ytrain[i]-prediction)*prediction*(1-prediction)*1.0
        b1=b1+alpha*(ytrain[i]-prediction)*prediction*(1-prediction)*x1[i]
        b2=b2+alpha*(ytrain[i]-prediction)*prediction*(1-prediction)*x2[i]
    epoch=epoch-1

    


# In[154]:


b0,b1,b2


# In[155]:


x3=xtest[:,0]
x4=xtest[:,1]
print(ytest)
y_pred=[0]*len(xtest)
for i in range(len(xtest)):
    y_pred[i]=np.round(1/(1+np.exp(-(b0+b1*x3[i]+b2*x4[i]))))
    print(np.round(y_pred[i]))


# In[156]:


from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,y_pred))


# In[ ]:





# In[ ]:





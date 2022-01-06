#!/usr/bin/env python
# coding: utf-8

# In[62]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'C:\Users\saaks\OneDrive\Desktop\Iris.csv')
df


# In[63]:


df.describe()


# In[64]:


species = df["Species"].tolist()
X = df.drop("Species", 1)


# In[65]:


# Standardize the data
X = (X - X.mean()) / X.std(ddof=0)
X


# In[66]:


covariance=np.dot(X.T,X)/(X.shape[0]-1)
print(covariance)


# In[67]:


eigenvalues,eigenvector=np.linalg.eig(covariance)
print("eigenvalues \n",eigenvalues)
print("eigenvector \n",eigenvector)


# In[68]:


eigenvector=eigenvector.T
print("eigenvector after Transpose\n",eigenvector)
indexs=np.argsort(eigenvalues)[::-1]
#taking those indices and storing in eigenvalues and eigenvectors accordingly
eigenvector=eigenvector[indexs]
print("eigenvector after indexes \n",eigenvector)
eigenvalues=eigenvalues[indexs]
print("eigenvalues \n",eigenvalues) 


# In[69]:


total = sum(eigenvalues)
variance_of_each_feature =(eigenvalues / np.sum(eigenvalues))*100
print("variance of each feature-->",variance_of_each_feature)
plt.figure(figsize=(8,4))
plt.bar(range(5),variance_of_each_feature, alpha=0.6)
plt.ylabel('Percentage of explained variance')
plt.xlabel('Dimensions')


# In[70]:


features=eigenvector[:2]
print("features",features)


# In[71]:


np.dot(X,features.T)


# In[96]:


pc1=X.dot(eigenvector.T[0])
pc2=X.dot(eigenvector.T[1])
res=pd.DataFrame(pc1,columns=["PC1"])
res["PC2"]=pc2
res['target']=species
res.head()


# In[98]:


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('PC1', fontsize = 15)
ax.set_ylabel('PC2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = res['target'] == target
    ax.scatter(res.loc[indicesToKeep,'PC1']
               , res.loc[indicesToKeep, 'PC2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()


# In[ ]:





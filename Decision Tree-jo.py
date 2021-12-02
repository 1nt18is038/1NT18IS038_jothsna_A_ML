#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ['hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone','breathes','venomous','fins','legs','tail','domesic','catsize','type']
pima = pd.read_csv("zoo_data.csv", header=None, names=col_names)
featured_cols=['hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone','breathes','venomous','fins','legs','tail','domesic','catsize']
X=pima.values[:,:16]
Y=pima.values[:,-1]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1) # 70% training and 30% test
dec=DecisionTreeClassifier()
dec=dec.fit(X_train,Y_train)
Y_pred=dec.predict(X_test)


print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred))
print("Confusion Matrix:\n ",
        confusion_matrix(Y_test, Y_pred))

target_names=['1','2','3','4','5','6','7']
from sklearn.metrics import classification_report
print(classification_report(Y_test,Y_pred,target_names=target_names))

from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus 
dot_data = StringIO()
export_graphviz(dec, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names =featured_cols,class_names=['1','2','3','4','5','6','7'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('ZOO.png')
Image(graph.create_png())


# In[63]:


featured_cols=['hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone','breathes','venomous','fins','legs','tail','domesic','catsize']
X=pima.values[:,:16]
print(X)


# In[64]:


Y=pima.values[:,-1]
print(Y)


# In[65]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1) # 70% training and 30% test
dec=DecisionTreeClassifier()
dec=dec.fit(X_train,Y_train)
Y_pred=dec.predict(X_test)
print(Y_pred)
print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred))

clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# In[66]:


from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus 
featured_cols=['hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone','breathes','venomous','fins','legs','tail','domesic','catsize']
dot_data = StringIO()
export_graphviz(dec, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names =featured_cols,class_names=['1','2','3','4','5','6','7'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png())


# In[67]:


pip install pydotplus


# In[68]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ['hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone','breathes','venomous','fins','legs','tail','domesic','catsize','type']
pima = pd.read_csv("zoo_data.csv", header=None, names=col_names)
featured_cols=['hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone','breathes','venomous','fins','legs','tail','domesic','catsize']
X=pima.values[:,:16]
Y=pima.values[:,-1]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1) # 70% training and 30% test
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ['hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone','breathes','venomous','fins','legs','tail','domesic','catsize','type']
pima = pd.read_csv("zoo_data.csv", header=None, names=col_names)
featured_cols=['hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone','breathes','venomous','fins','legs','tail','domesic','catsize']
X=pima.values[:,:16]
Y=pima.values[:,-1]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3) # 70% training and 30% test

clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Train Decision Tree Classifer
clf = clf.fit(X_train,Y_train)

#Predict the response for test dataset
Y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred))

from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus 
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names =featured_cols,class_names=['1','2','3','4','5','6','7'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('ZOO.png')
Image(graph.create_png())

target_names=['1','2','3','4','5','6','7']
from sklearn.metrics import classification_report
print(classification_report(Y_test,Y_pred,target_names=target_names))


# In[69]:


target_names=['1','2','3','4','5','6','7']
from sklearn.metrics import classification_report
print(classification_report(Y_test,Y_pred,target_names=target_names))


# In[ ]:





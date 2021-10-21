#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World!")


# In[2]:


a=10
print(a)


# In[3]:


a="Jothsna Sai"
print(a)


# In[4]:


a=10
if a>10:
    print("Greater")
else:
    print("lesser")


# In[5]:


a=5
b=5
print(a+b)


# In[6]:


a=10
b=10.00
print(a+b)


# In[12]:


a=5
b=6
print("a:",a,"b:",b)
a=a+b
b=a-b
a=a-b
print("a:",a,"b:",b)


# In[ ]:





# In[9]:


a=5
b=6
print(a)
print(b)
a=a+b
b=a-b
a=a-b
print(a)
print(b)


# In[13]:


a=int(input("Enter a number:"))
print(a)
type(a)


# In[14]:


for i in range(1,10):
    print(i)


# In[23]:


a=int(input("enter number1:"))
b=int(input("enter number2:"))
c=input("enter operator:")
if c=='+':
    print(a+b)
elif c=='-':
    if(a>b):
        print(a-b)
    else:
        print(b-a)
elif c=='*':
    print(a*b)
elif c=='/':
    if(b==0):
        print("Not Valid")
    else:
        print(int(a/b))
elif c=="%":
    print(int(a%b))
else:
    print("Invalid")


# In[42]:


def find(word):
    words=["Pen","Pencil","Eraser","Book"]
    for l in words:
        if(l.lower()==word.lower()):
            print("Found")
            return
    print("Not Found")
    
find("pencil")dict[key]


# In[40]:


str1="I am"
str2=" Jothsna sai"
print(str1+str2)


# In[45]:


str1="abc"
str2="abc"
if str1>str2:
    print(str1,"is greater than",str2)
elif str1<str2:
     print(str1,"is less than",str2)
else:
    print("Both are equal")
    


# In[46]:


str1="Jothsna sai"
print(str1[::-1])


# In[48]:


def reverse(word):
    rev=""
    for letter in word:
        rev=letter+rev
    return rev

reversed=reverse("Jothsna sai")
print(reversed)


# In[49]:

dict[key]
a="Josh"
b="josh"
print(bool(a<b))


# In[53]:


a=[1,2,3,4,5,6,7,8,9]
x=slice(0,10,2)
print(a[x])


# In[61]:


list=["apple","Orange","Banana","Jackfruit"]
print(list[::-1])


# In[59]:


a=[1,2,3,4,5,6,7,8,9]
list=["apple","Orange","Banana","Jackfruit"]
print(a+list)


# In[57]:


def copyingstring(word):
    str=word
    print("Copied string is",str)
    
copyingstring("Machine Learning")


# In[68]:


a=[1,2,3,4,5,6,7,8,9]
a.append(10)
a.remove(1)
a.pop()
print(a)


# In[77]:


dict={'abc':1,'efg':2,'hij':3}
dict['xyz']=4
print(dict)


# In[78]:


tuple=(1,2,3,4,5)
print(max(tuple))


# In[75]:


list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1)


# In[80]:


# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p' 
print(my_tuple[5])   # 't'

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4


# In[93]:


dict={"one":"deepti","two":"Faizah"}
for key,value in dict.items():
    print(key,value)
for i in dict.values():
    print(i)
for i in dict:
    print(i)


# In[ ]:





# In[ ]:





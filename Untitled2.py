#!/usr/bin/env python
# coding: utf-8

# In[3]:


sortList = [23,24,89,6,9]


# In[5]:


sortList.sort(reverse=True)
sortList


# In[6]:


newList = [23,65,78,3,4,6]


# In[8]:


newList.reverse()
newList


# In[9]:


newList.clear()
newList


# In[10]:


newList = ['hamza','ahsan','khizar','x']


# In[11]:


newList.sort()
newList


# In[12]:


bList = ['A','b','F']


# In[13]:


bList.sort()
bList


# In[14]:


cList = [23,78,84,87,98]


# In[16]:


x = cList.pop()


# In[19]:


print(cList)
print(x)


# In[20]:


cList =[23,78,84,87,98] 


# In[21]:


y = cList.pop(2)


# In[23]:


print(cList)
print(2)


# In[24]:


aList = ['oranges','lehsun','banana']


# In[25]:


aList.remove('lehsun')


# In[26]:


aList


# In[27]:


sortList = [23,56,67,23,22,45]


# In[28]:


sortList.sort()
sortList


# In[29]:


cList = [23,35,76,98,24]


# In[34]:


dList=[]


# In[46]:


x = cList.pop()


# In[47]:


dList.append(x)


# In[48]:


print(cList)
print(dList)


# In[64]:


cList = [23,67,87,98,64]


# In[65]:


dList=[]


# In[92]:


x = cList.pop()


# In[93]:


dList.append(x)


# In[94]:


print(cList)
print(dList)


# In[101]:


cList = [23,67,87,98,64]
emptyList=[]


# In[112]:


emptyList.append(cList.pop())


# In[113]:


print(emptyList)


# In[114]:


#practise apply if else statement in cList cell ln[101]


# In[123]:


a = [23,67,87,98,64]
b = []


# In[130]:


if len(a)!=0:
    b.append(a.pop())
    print(a)
    print(b)
else:
    print("list is empty now  cannot be popped")


# In[131]:


#if else statement done 


# In[132]:


#to do list 


# In[133]:


#take input if work is done
#if yes then task will be eliminated
#and append in finished task
#if no code should not crash
#apply if else condition


# In[134]:


b


# In[142]:


c=b #pass by reference


# In[136]:


c


# In[139]:


del b[3]


# In[140]:


b


# In[141]:


c


# In[157]:


d=c.copy() #copy refernce


# In[144]:


d


# In[145]:


del c[2]


# In[146]:


c


# In[147]:


d


# In[148]:


b=[53,74,76,73]


# In[149]:


d=b.copy()


# In[150]:


d


# In[153]:


del b[3]


# In[154]:


b


# In[155]:


d


# In[156]:


#slicing


# In[158]:


d


# In[160]:


d[1]


# In[161]:


d=[5454,77,978,37]


# In[162]:


d[2]


# In[163]:


d[1:4]


# In[164]:


d


# In[165]:


#direction of slicing is always left to right
#there are no errors in slicing it will show empty


# In[169]:


d=[623,642,756,654,673,873,645,736,635,836]


# In[170]:


print(d)
d[1:8:3]


# In[171]:


#reverse indexing


# In[189]:


cities = ["khi","lhr","multan","pindi","islamabad","hyderabad"]
#index     -6    -5     -4       -3       -2         -1


# In[184]:


cities[-5]


# In[185]:


cities[3]


# In[186]:


print(cities)
cities[-4:-2]


# In[187]:


#starting point empty and ending 5 means o to 4


# In[190]:


cities[-5:1]


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


#Data used
#Changed one value to have a higher negative to show the absolute value loop works
Data = [0, -1, 2, -3, 4, -10, 6, -7, 8]
total = 0


# In[5]:


#Basic matplot functionality
plt.hist(Data)
plt.title("Histogram!")


# In[66]:


#Prints out the total sum for the dataset
for i in Data:
    total += i
print(total)

    


# In[51]:


#Computing the mean
for i in Data:
    total += i/len(Data)
print(total)


# In[67]:


#Printing the absolute value 
for i in Data:
    total += i
print(abs(total))


# In[80]:


x = 144
y = 9

epsilon = 1


# In[2]:


if x < 0:
    print("does not exist")
else:
    high = max(1,x)
    low = 0
    ans = (high + low)/2
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2
    print(ans, 'is close', x)


# # Functions

# Here we have a funtion that returns the greatest value between two vaariables. It is very simple as it contains a if else statement with selected parameters built into the def.From there you can call the function later in the script to test the max between the two. This is a very basic example as it could include more variables.

# In[3]:


def max_v(x,y):
    if x > y:
        print("X is greater")
    else:
        print("y is greater")
        


# In[4]:


max_v(x,y)


# This function is more advanced and what it does is returns the closest square root it can find. Working through the function created you can see it takes in three different inputs being x, power and epsilon. What this does in the first if statement is tests to see if x is less than zero and power is an even number. If both are turn it will return none.
# 
# The second part we can see it takes high and low being the min and max between x and -1 for min and max. 

# In[1]:


def find_root(x,power, epsilon):
    if x < 0 and power%2 == 0:
        return None
    low = min(-1,x)
    high = max(1,x)
    #Bisection search
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power <x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans
    


# In[2]:


find_root(10,4,.01)


# In[24]:


max(-1,x)


# In[28]:


(high + low)/2


# In[68]:


abs(ans**power - x)


# In[ ]:





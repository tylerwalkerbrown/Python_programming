#!/usr/bin/env python
# coding: utf-8

# # Chapter 3/ Week 4 Basic Code

# In[ ]:


#Math package
import math as m 


# In[39]:


#Numbers we will use as an example throughout the sheet
x= 6
y = 8
z = 12


# Below we have an exhaustive enumerator example that we find in the book section 3.1. You can see some different examples of arithmetic operators being used to compute whether or not the number is a perfect cube.

# In[11]:


#x = int(input('Enter some numba:'))
ans = 0 
while ans**3 < abs(x):
    ans = ans + 1 
if ans**3 != abs(x):
    print(x,'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
        print('cube root of', x,'is', ans)
        print('Value of the decrementing function abs(x) - ans**3 is', abs(x) - ans**3)


# Here wen have a for loop that allows us to print ranges. Since python uses index as the range I have added a modification to give +1 to make it easier for the user to understand how it works. I also made it an input number so it can be changed to whatever range you need as seen below.
# 

# In[13]:


#Prints from 0 to input number
# if statement is useless in this case as it prints out same result with less code
rng = int(input('Range to:'))
for i in range(1+ rng):
    print(i)


# In[ ]:


#Task 2 
rng = int(input('Range to:'))
for i in range(rng + 1):
    print(i)


# In[ ]:


#Task 1 print 1-5
#(start,stop,step)
list(range(1,6))


# In[31]:


#Task 2 
a = int(input("First number"))
b= int(input("Second Number"))
summ = a +b
print(summ)


# In[32]:


# Task 3 
#Pie squared using m from math package
summ = m.pi**2
print(summ)


# In[34]:


#Task 4 
summ = m.cos(30) + m.sin(30)
print(summ)


# In[51]:


#Task 5
#left justified columns
print('%6d %6d %6d' %(x,y,z))


# In[37]:


#Task 6
#Area of a circle 
r = int(input("What is the radius of the circle:"))
area = (m.pi) * r **2
print(area)


# In[38]:


#Task 7 
#Pirnting out which number is greater between the two 
x = 5
y = 10
if x > y:
    print('x is greater')
else:
    print('y is greater')


# In[57]:


#Task 8 
A = 1
B = 10
result = not(A and B)
print(result)


# In[21]:


#Task 9
non_zero = list(range(1,11))
total = 0
for i in non_zero:
    total += i
print(total)


# In[24]:


#Task 10
tot = 0 
num = 1 
while num <= 10: 
    tot += num
    num += 1    
print (tot)


# # Chapter 3 Enumerators

# Below we have an example of an exhaustive enumerator. What this particualar one does is tests the cubed root of ever number before our input number being (a). It does this with a while look with built in conditions below. In while expression it iterates testing every intrement of 1. Then if the cubed root does not equal to teh absolute values of the input number then it will come up displaying a simple message indicating it is not a perfect cube. Then for all else it simply passes it through an if statement that could go either way less than or greater than 0 and assigning ans to ans to then print it out at the bottom.

# In[1]:


a = int(input("Enter input:"))
ans = 0 
while ans**3 <(a):
    ans = ans + 1 
if ans**3 != abs(a):
    print(a, 'just didnt make the cut as a perfect cube')
else: 
    if a > 0:
        ans = ans
        print('Cube root of', a ,'is', ans)


# Below is an example of an enumarator that checks to see if a number is prime or not. What this does is creates a range initially of a list of numbers to check. From there it takes your input and checks to see what number if any is divisible a number in the guess range.

# In[7]:


b = int(input('What do you wanna check:'))
smallest = None
for guess in range(2,b):
    if b%guess == 0:
        smallest = guess
        break 
if smallest != None:
    print('Smallest divisor of', b , 'is', smallest)
else:
    print(b,'is a prime number')


# In[8]:


print('Value of the decrementing function abs(x) - ans**3 is', abs(x) - ans**3)


# In[ ]:


max_val = int(input('Enter a postive integer: ')) 
i =0
while i < max_val:
    i =i+1 
    print(i)


# In[19]:


import math as m 


# In[20]:


math = m.sqrt(25)


# In[21]:


math


# In[23]:


help("math")


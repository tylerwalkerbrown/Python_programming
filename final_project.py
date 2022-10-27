#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
profile = {}
n = random.randint(-100,100)
keepGameGoing = "yes"
numOfGuesses = 2
while keepGameGoing == "yes":
    name = str(input("Enter your name here: "))
    guess = int(input("Enter Guess: "))
    keepRoundGoing = True
    count = 0
    while keepRoundGoing == True:
        if guess == n:
            print("Congrats you did it")
            keepRoundGoing = False
            count +=1 
        elif count == numOfGuesses:
            print("You reached max guesses")
            keepRoundGoing = False
            count+=1

        elif guess < n:
            print("Too low")
            guess = int(input("Guess new num: "))
            count+=1
        else:
            print("Too high")
            guess = int(input("Guess new num: "))
            count+=1
        profile[name] = "Num of guesses: " + str(count) + " Actual answer: " + str(n)
    keepGameGoing = str(input("Do you want to continue: (yes or no) "))
    print("Updated Profile: " + str(profile))

print("Final Game Scores: " + str(profile))


# In[ ]:


str.split(profile)


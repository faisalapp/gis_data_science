#!/usr/bin/env python
# coding: utf-8

# # Assignement 2
# 

# Please do not change, delete or edit any cells. Write your code in between designated lines.
# 
# 

# ## Question 1 (10 points)

# In[1]:


# Can your print the letters of Agriculture by using for loops. Your output will look like this:
# A
# g
# r
# i
# c
# u
# l
# t
# u
# r
# e

## Your code here - down ##

test_data = "Agriculture"

for char in test_data:
    print(char)



## Your code here - up ##


# ## Question 2 (40 Points)

# In[2]:


# Find the sum of numbers from 1 to 50(including) by using for loops.

## Your code here - down ##

sum = 0

for num in range(1,51):
    sum = sum + num    
print(sum)

## Your code here - up ##


# ## Question 3 (50 points)

# In[4]:


# Now let's find sum of even and odd numbers from 1 to 50 (including). Are the results same?

# Sum of even  numbers

## Your code here - down ##

sum_even = 0

for num in range(1,51):
    if num % 2 == 0:
        sum_even = sum_even + num

print(sum_even)

## Your code here - up ##


# In[6]:


# Sum of odd numbers

## Your code here - down ##

sum_odd = 0

for num in range(1,51):
    if num % 2 != 0:
        sum_odd = sum_odd + num

print(sum_odd)

## Your code here - up ##


# In[7]:


# In this cell explain the difference.

# If the number is divisible by 2, it will be even number else odd number


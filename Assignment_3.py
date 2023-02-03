#!/usr/bin/env python
# coding: utf-8

# # Assignment 3

# Please do not change, delete or edit any cells. Write your code in between designated lines.

# ## Question 1 (15 points)

# In[1]:


# Create a dictionary named dict1 then add key and values.
# When you print output of dict1 will be shown as {'Peas': 55, 'Canola': 66, 'Oat': 65}.

## Your code here - down ##

dic1 = {}
dic1["Peas"] = 55
dic1["Canola"] = 66
dic1["Oat"] = 65

print(dic1)


## Your code here - up ##


# In[2]:


# In this cell you need to change the assigned value of Peas to 66 and print dict1 again.

## Your code here - down ##

dic1["Peas"] = 66
print(dic1)

## Your code here - up ##


# In[6]:


# Now use For Loop and print values and key inside dict1. Your output will look like:
# Peas
# 66
# and so on.

## Your code here - down ##

for key, value in dic1.items():
    print(key)
    print(value)

## Your code here - up ##


# ## Question 2 (30 points)

# In[18]:


ls = [2,7,9, 4]

# Method 1
# Ceate a list that consist of square of ls values.

## Your code here - down ##

ls_sqr_1 = []

for item in ls:
    ls_sqr_1.append(item ** 2)
    
print(ls_sqr_1)

## Your code here - up ##


# In[20]:


# Method 2

## Your code here - down ##

ls_sqr_2 = []

[ ls_sqr_2.append(item ** 2) for item in ls]

print(ls_sqr_2)


## Your code here - up ##


# ## Question 3 (55 points)

# In[28]:


import numpy as np

ar_1 = np.array([[3, 4, 5],
                 [3, 4, 5]])
# What is shape of the array?

## Your code here - down ##

ar_1.shape

## Your code here - up ##


# In[49]:


ar_2 = np.array([[3, 4, 5],
         [8, 4, 1]])
# Print first row of ar_2

## Your code here - down ##

ar_2[0]

## Your code here - up ##


# In[51]:


# Write a code that will print 1 in ar_2.

## Your code here - down ##

ar_2[1,2]

## Your code here - up ##


# In[53]:


# Print entire mean of ar_2

## Your code here - down ##

np.mean(ar_2)

## Your code here - up ##


# In[54]:


# Print each columns' mean

## Your code here - down ##

np.mean(ar_2, axis=0)

## Your code here - up ##


# In[57]:


# Print entire standard deviation  of ar_2

## Your code here - down ##

np.std(ar_2)
## Your code here - up ##


# In[62]:


# Print each rows' standard deviation.

## Your code here - down ##

np.std(ar_2, axis=1)

## Your code here - up ##


# In[61]:


# Find the difference between mean and median of entire ar_2.

## Your code here - down ##

mean = np.std(ar_2)
median = np.median(ar_2)

diff = median - mean
print(mean)
print(median)
print(diff)

## Your code here - up ##


# Are mean and median same? If they are different, explain what does that mean.
# 
# Please explain below in this cell only.
# 
# Mean and Median are two different things. Mean is the average of all numbers (sum of numbers divided by number count) while Median is calculated by sorting numbers then picking number in the middle (if number count is odd) or average of two numbers in the middle (if number count is even) 
# 

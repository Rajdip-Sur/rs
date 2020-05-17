#!/usr/bin/env python
# coding: utf-8

# # Session 1: Assignment 1
# #task 1
# 
# #1.Install Jupyter notebook and run the first program and share the screenshot of the output.

# In[6]:


print('my first programm')


# In[ ]:





# In[ ]:





# # 2.
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

# In[8]:


for i in range(2000,3201):
    if i%7==0 and i%5 !=0:
        print(i,end=',')


# In[ ]:





# # 3.
# Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name

# In[11]:


a=input('Enter your first name:-')[::-1]
b=input('Enter your last name:-')[::-1]
print(f'{b} {a}')


# In[ ]:





# # 4.
# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r
# 3

# In[12]:


import math


# In[14]:


pi=math.pi
v=4/3*pi*(12/2)**3
v


# In[ ]:





# # Task 2:
# 1.
# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

# In[15]:


r=str(input('enter comma-separated numbers:-'))
r.split(',')


# In[ ]:





# In[35]:


'''# 2.Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*'''


# In[24]:


for i in range(1,6):
    print('*'*i)
for j in range(5,0,-1):
    print('*'*j)


# In[ ]:





# # 3.
# 3.Write a Python program to reverse a word after accepting the input from the user.

# In[27]:


a=input("Enter anything:-")[::-1]
a


# In[ ]:





# # '''4.
# Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens#
# Sample Output:
# WE, THE PEOPLE OF INDIA,
#     having solemnly resolved to constitute India into a SOVEREIGN,!
#         SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
#          and to secure to all its citizens'''

# In[33]:


print('WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN, !\n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t and to secure to all its citizens')


# In[ ]:





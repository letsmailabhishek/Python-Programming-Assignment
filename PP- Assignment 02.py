#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python program to convert kilometers to miles');get_ipython().run_line_magic('pinfo', 'miles')


# In[1]:


#ANS:
a=float(input("Enter the value in kilometers ",))

#To convert the kilometer to mile 
#'x' kilometers = (0.621371x) miles
miles=0.621371*a

print(a, "kilometer is ",miles,"miles")


# In[ ]:


get_ipython().set_next_input('2. Write a Python program to convert Celsius to Fahrenheit');get_ipython().run_line_magic('pinfo', 'Fahrenheit')


# In[2]:


#ANS:
a=float(input("Enter the value of Celsius ", ))

#To convert the value we follow the below formula.
Fahrenheit=(9/5*a)+32

print(a," degree Celsius is equal to",Fahrenheit,"degree Fahrenheit")


# In[ ]:


get_ipython().set_next_input('3. Write a Python program to display calendar');get_ipython().run_line_magic('pinfo', 'calendar')


# In[4]:


import calendar
year=2023
month=1

print(calendar.month(year,month))


# In[ ]:


get_ipython().set_next_input('4. Write a Python program to solve quadratic equation');get_ipython().run_line_magic('pinfo', 'equation')


# In[6]:


#ANS:
import cmath
a=int(input("Enter the value ",))
b=int(input("Enter the value ",))
c=int(input("Enter the value ",))

d=((b**2)-(4*a*c))

sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)

print("The first solution is ",sol1)
print("The second solution is ",sol2)


# In[ ]:


get_ipython().set_next_input('5. Write a Python program to swap two variables without temp variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[7]:


#ANS:
a=float(input("Enter the value of 1st variable ",))
b=float(input("Enter the value of 2nd variable ",))

#value of the variable before swapping
print("Values of the variables before swapping")
print("Value of a is ",a)
print("Value of b is ",b)


#value of the variable after swapping
a,b=b,a
print("Values of the variables after swapping")
print("Value of a is ",a)
print("Value of b is ",b)


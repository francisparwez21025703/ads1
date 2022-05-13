#!/usr/bin/env python
# coding: utf-8

# Question 1

# In[ ]:



# separator needs to be specified
shour, sminu, ssec = input("Enter the time in HH:MM:SS format: ").split(":")

# use of min as name would overwrite the built-in function min()
hour, minu, sec = int(shour), int(sminu), int(ssec)
print ("hour =", hour, "minute =", minu, "second =", sec)


# Alternative

# In[ ]:


# store the complete time string first
time = input("Enter the time in HH:MM:SS format: ")
# separator needs to be specified
shour, sminu, ssec = time.split(":")

# use of min as name would overwrite the built-in function min()
hour, minu, sec = int(shour), int(sminu), int(ssec)
print ("hour =", hour, "minute =", minu, "second =", sec)


# Question 2

# In[ ]:


import numpy as np

for radius in range(2, 21, 2):  # stop needs to be 21 or 22
    area = 4.0 * np.pi * radius**2
    volume = 4.0 / 3.0 * np.pi * radius**3
    print ("radius =", radius, "  area =", area, "volume =", volume)


# Question 3

# In[ ]:


sum = 0.0  #  needs to have a value before the loop starts

for i in range (3):
    num = float(input("Enter a number: "))
    sum = sum + num

print ("The sum is", sum)
print ("The average is ", sum/3.0)


# Question 4

# In[ ]:


import numpy as np


def vol_radius(r):
    """ Calculates the volume of a sphere from its radius """
    
    vol = 4. / 3. * np.pi *r**3
    return vol


def vol_diameter(d):
    """ Calculates the volume of a sphere from its diameter """
    
    vol = 4. / 3. * np.pi *(d/2.0)**3
    return vol
    
# main program starts here
x = float(input("Enter radius or diameter " ))
choice = input("Enter r for radius or d for diameter " )

# nothing will happen if input is not r or d
if choice == "r":
    print("The volume is", vol_radius(x))
elif choice == "d":
    print("The volume is", vol_diameter(x))
    


# In[ ]:


import numpy as np


def vol_radius(r):
    """ Calculates the volume of a sphere from its radius """
    
    vol = 4. / 3. * np.pi *r**3
    return vol


def vol_diameter(d):
    """ Calculates the volume of a sphere from its diameter """
    
    vol = 4. / 3. * np.pi *(d/2.0)**3
    return vol
    
# main program starts here
choice = "d"   # choice needs to preset with a value giving a True value for while

while choice == "d" or choice == "r":

    x = float(input("Enter radius or diameter " ))
    choice = input("Enter r for radius or d for diameter " )

    # nothing will happen if input is not r or d
    if choice == "r":
        print("The volume is", vol_radius(x))
    elif choice == "d":
        print("The volume is", vol_diameter(x))
    print()     # empty line
    


# Question 6

# In[ ]:


def factorial(n):
    """
    Returns the factorial of the argument using a simple loop
    """
    
    fac = 1
    for i in range(1, n+1):  # start at 1 and multiply up to n
        fac = fac * i
    return fac
    
# main program
number = int(input("Enter a number: "))
print ("n! =", factorial(number))


# Question 7

# In[ ]:


text = "University of Hertfordshire"

print(text[9])
print(text[14])
print(text[-1])


# Question 8

# In[ ]:


text = "University of Hertfordshire"

print(text[14:27])

# alternative
print(text[14:])


# Question 9

# In[ ]:


# part a
shopping = ["bread", "butter", "boomerang", "beans", "broccoli"]
print (shopping)
print()

# part b
# remember Python counts from 0
print (shopping[3])
print()

# part c
# numbering for slicing different from indexing. Confusing, I know.
print (shopping[2:4])
print()

# part d
shopping[4] = "blueberry"
print (shopping)
print()

# alternative way
shopping[-1] = "blackcurrant"
print (shopping)    
print()

# part e
shopping.append("banana")
print (shopping)


# In[ ]:





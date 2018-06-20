#What is Time Tuple?
import time

print(time.gmtime(0))

#Write a program to get formatted time.

import time;

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


#Extract month from the time.

from datetime import datetime

now=datetime.now()

print("month:",now.strftime("%B"))

#Extract day from the time.


from datetime import datetime

now=datetime.now()

print("day:",now.strftime("%A"))



#Extract date (ex : 11 in 11/01/2021) from the time.


import datetime

d= datetime.date.today()
print(d)
print(d.day)


#Write a program to print time using localtime method.

import time

print(time.asctime(time.localtime()))


#Find the factorial of a number input by user using math package functions.

import math

n=int(input("enter the number whose factorial you want to calculate:"))

print("answer is:",math.factorial(n))


#Find the GCD of a number input by user using math package functions.

import math

n=int(input("enter the first number:"))
p=int(input("enter the second number:"))

print("result:",math.gcd(n,p))


#Use OS package and do the following tasks: 
#Get current working directory.
#Get the user environment.

import os

print("current working directory:",os.getcwd())
print("environment variables are:",os.environ)
#Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import threading
from threading import Thread
import time


def display():
    for x in range(2):
      print(threading.current_thread().getName(),":","hello world")
      time.sleep(5)

t=Thread(target=display)
t.start()


for x in range(2):
    print(threading.current_thread().getName(),":","hello world")
    time.sleep(5)


#Make a thread that prints numbers from 1-10, waits for 1 sec between
import threading
from threading import Thread
import time


def display():
    for x in range(1,11):
      print(x)
      time.sleep(1)

t=Thread(target=display)
t.start()



#Make a list that has 5 elements.
#Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec
import threading
from threading import Thread
import time
def display(l):
    t=2
    for x in l:
        print(x)
        time.sleep(t)
        t=t+2
l=[2,3,6,9,1]
t3=Thread(target=display,args=(l,))
t3.start()



#Call factorial function using thread.
import threading
from threading import Thread
import time
import math
def fact():
     fact=1
     for x in range(1,num+1):
         fact=fact*x
     print("The factorial of",num,"is",fact)

num=int(input("Enter any  number: "))
t4=Thread(target=fact)
t4.start()

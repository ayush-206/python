#prog to take input year from user and decide whether it is leap or not
year=int(input("enter any year"))
if(year%400==0)or(year%4==0)and(year%100!=0):
 print("year is leap")
else:
 print("year is not leap")
 
#take length and breadth input from user and check dimension are of square or rectangle
l=int(input("enter any length"))
b=int(input("enter any breadth"))
if(l==b):
 print("dimension are of square")
else:
 print("dimension are of rectangle")
 
#take ther input ager of 3 people and determnine the youngest and oldest in them
a=inut("enter your age"))
b=int(input("enter your age"))
c=int(input("enter your age"))
if(a>b):
 if(a>c):
  print("a is older")
 else:
  print("c is older")
 else:
  if(y>z):
   print("y is older")
  else:
   print("z is older")
#create a list with user defined inputs
x=int(input("enter the value of x"))
y=int(input("enter the value of y")) 
z=int(input("enter the value of z"))

l=[x,y,z] 
print(l)

#add the following list to above created list
x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
z=int(input("enter the value of z"))
l1=[x,y,z]
l2=['google",apple",facebook",microsoft",tesla']
l=l1+l2
print(l)

#count the number of timean object occurs in a list
x=[1,2,3,1,4,5,6,1,9,8]
print(x.count(1)) 

#create a list with number and sort in ascending order
s=[2,5,7,4,3,8,9]
s.sort()
print(s)

#program to merge two one dimensional array in sorted manner
a=[7,2,5,6]
a.sort()
print(a)
b=[9,4,3,8]
b.sort()
print(b)
c=a+b
c.sort()
print(c)
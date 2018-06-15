#program to create tuple with different datatype 
#find the length of tuples
a=(1,2,3)
print(len(a))

#find the largest and smallest element of tuples
a=(1,2,3)
print(max(a))
print(min(a))

#program to find the product of all element of tuple
def  pro(t):
 r=1
 for i in t:
  r=r*i
 return r
tu=(1,2,3)
p=pro(tu)
print(p)

#calculate two set using user defined values
#1)calculate difference between two sets
a1=set([1,2,3,4,5,6]) 
a2=set([2,3,5,8,9,5])
print(a1-a2)

#2)print the result of intersection of two sets
a1=set([1,2,3,4,5,6])
a2=set([2,3,5,8,9,5])
print(a1&a2)

#create a dictionary to store name and marks of 10 student by user input
d={}
for n in range (10):
  name=input("enter your name:")
  marks=int(input("enter your marks:"))
d[name]=marks
print(d)  

#sorting of dictionary
d={'a':20,'b':30,'c':40}
values=list(d.values())
print(values)
values.sort()
print(values)

#count the no. of occurence of each letter in word "MISSISSIPPI"
l=list("MISSISSIPPI")
d={}
d['m']=l.count('m')
d['i']=l.count('i')
d['s']=l.count('s')
d['s']=l.count('s')
d['i']=l.count('i')
d['s']=l.count('s')
d['s']=l.count('s')
d['i']=l.count('i')
d['p']=l.count('p')
d['p']=l.count('p')
d['i']=l.count('i')
print(d)
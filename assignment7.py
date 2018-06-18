#calculate the area of circle by taking radius from the user
# def area():
 # r=int(input("enter the radius"))
 # area=3.14*r*r
 # print(area)

# area ()

 #prog to finding the perfect number in range between 1/1000 
def perfect(n):
  sum=0
  for i in range(1,n):
    if n%i==0:
      sum=sum + i
  if sum==n:
    return True
  else:
    return False
for i in range(1,1001):
  if perfect(i):
    print( i)
	

# Q.3- Print multiplication table of 12 using recursion.

def table(n,i):
  print (n*i)
  i=i+1
  if i<=10:
    table(n,i)
table(12,1)


 # Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(a,b):
  if b == 1:
    return a
  else:
    return a*power(a,b-1)
print (power(6,2))


# Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
c=factorial(n)
l="output"
d={}
d[l]=c
print(d)
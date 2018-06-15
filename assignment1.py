#Git Commands
git config --global user.name"your name"
git config --global user.email"email"
git init
git add fie name #this is for selective approch
git add . #this is for adding all file
git status 
git commit -m"message"
git add origin master "link from our git repository"
git push origin master

#git updation
git add .
git commit -m"message"
git status
git push origin master




# assignment-5


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
a=int(input("enter your age"))
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
   
 #4.Write an if statement to lets competitor know which of these prizes they won.
a=int(input("Enter the points:"))
f=1
if a<200:
    if 1<a<50:
        f=0
        print("No Prize")
    elif 50<a<150:
        prize="Wooden Box"
    elif 150<a<180:
        prize="Book"
    elif 180<a<200:
        prize="Chocolate"
    if f!=0:
        print("Congratulations! You won a {}".format(prize))
 
#prog to print total cost for user 
n=int(input("enter the cost:"))
p=n*100
if p>1000:
   disc=p*.1
   r=p-disc
   print('total cost= ',r)




# q1 take 10 integers from user and print them on screen.

for x in range(10):
    x = int(input("enter the numbers "))
    print(x)

q2 write an infinite loop. an infinite loop never ends. the condition is always true.

i = 1
while (i < 10):
    print(i)

# q3 create a list of integer elements by user input.make a new list which will store the squares of elements of previous list.
l = []
for x in range(5):
    x = int(input("enter the values"))
    l.append(x)
print(l)
new = []
i = 0
for x in range(5):
    new.append(l[i] ** 2)
    i += 1
print(new)

# q4 form a list containing ints , strings and floats.make three lists to store them separately.
l = []
for x in range(0, 3):
    x = int(input("enter numbers"))
    l.append(x)
for x in range(3, 6):
    x = input("enter strings")
    l.append(x)
for x in range(6, 9):
    x = float(input("enter floats"))
    l.append(x)
print(l)
l1 = []
l2 = []
l3 = []
for x in l:
    if type(x) == int:
        l1.append(x)
    elif type(x) == str:
        l2.append(x)
    elif type(x) == float:
        l3.append(x)
print(l1)
print(l2)
print(l3)

# q5 using range(1,101),make a list containing odd and even numbers.

lo = []
le = []
print("odd numbers in given range are:")
for x in range(1, 101):
    if x % 2 == 0:
        le.append(x)
    else:
        lo.append(x)
print("even list:", le)
print("odd list:", lo)

# q6 print the followinf pattern.

i = 1
while (i <= 10):
    j = 1
    while (j <= i):
        print("*", end="")
        j = j + 1
    i = i + 1
    print()

# q7 ceate a user defined dictionary and get keys corresponding to values using loop.

d = {}
for x in range(5):
    keys = int(input("enter the keys"))
    values = input("enter value items")
    d[keys] = values
print(d)

# q8Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.


l = []
flag = 0
for x in range(5):
    x = int(input("enter the numbers"))
    l.append(x)
print(l)
y = int(input("select any number you want to search"))
for x in l:
    if x == y:
        l.remove(x)
        flag = 1
print(l)
if flag == 0:
    print("the number you entered is not in the list")




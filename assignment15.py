#QUESTION:1 Extract the user id, domain name and suffix from the following email addresses. 
#            emails = "zuck26@facebook.com" "page33@google.com"
#                      "jeff42@amazon.com"
#     desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]
#SOLUTION:
import re
emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
p=re.compile(r"(.*)@(.*).(...) (.*)@(.*).(...) (.*)@(.*).(...)")
result=p.match(emails)
a=(result.group(1))
b=(result.group(2))
c=(result.group(3))
d=(result.group(4))
e=(result.group(5))
f=(result.group(6))
g=(result.group(7))
h=(result.group(8))
i=(result.group(9))
A=[a,b,c]
B=[d,e,f]
C=[g,h,i]
l=[tuple(A),tuple(B),tuple(C)]
print(l)



#QUESTION:2 Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#          text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter,
#                  To make the bitter butter better." 
#SOLUTION:
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter,To make the bitter butter better."
p=re.compile(r"B",re.I)
result=p.finditer(text)
for r in result:
	print(r)
	
	
 
#QUESTION:3 Split the following irregular sentence into words 
#             sentence = "A, very very; irregular_sentence"
#            desired_output = "A very very irregular sentence"
#SOLUTION:
import re
sentence = "A, very very; irregular_sentence"
m=re.sub(r"[^\w]"," ",sentence)
p=re.sub("_"," ",m)
print(p)
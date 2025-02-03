import math
s=input("Enter a value: ")
sum=0
for i in s:
   sum+=math.factorial(int(i))
if sum == int(s):
  print(s,"is a krishnamurthi number")
else:
  print(s,"is not a krishnamurthi number")

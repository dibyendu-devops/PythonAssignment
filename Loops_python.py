We have two types of loops in python
1: While Loop::
# --> Write a code to print all the values from 1 to 100 and skip the numbers are divisible to 3 and 5
i = 1
while i <= 100:
    if i % 3 and i % 5:
        print(i)
    i= i+1

j = 1
while j <= 4:
    print("Dibyendu ",end="")
    k =1
    while k <= 1:
        print(" Mahatha ", end = "")
        k=k+1
    j = j+1
    print()

Out:: 
Dibyendu Mahatha
Dibyendu Mahatha
Dibyendu Mahatha
Dibyendu Mahatha



Print the below pattern::
#  #  #  #  # 
#  #  #  #  # 
#  #  #  #  # 
#  #  #  #  #

j = 1
while j <= 4:
    print("# ",end="")
    k =1
    while k <= 4:
        print(" # ", end = "")
        k=k+1
    j = j+1
    print()



#########################################
FOR LOOP: for loops work on dictory,list, array and with string

x = "DIBYENDU"
y = ['Dibyendu', 45, 6.7, 43]
for i in x:
	print(i)
for i in y:	
	print(i)

for i in range(20,10,-1):
    print(i)
  
for i in range(0,10,1):
    print(i)
#print a range 1 to 20 and which is not divisible by 5
for i in range (1,21):
    if i%5 !=0:
        print(i)

#print all the perfect square number between 1 to 500:

for i in range (1,500):
    if i**2 <=500:
        print(i**2)

  Using math function::
import math
for i in range(1,500):
    a=math.sqrt(i)
    if i%a==0:
        print(i)

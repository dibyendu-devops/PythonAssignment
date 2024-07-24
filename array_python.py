from array import *

vals = array('i',[5,9,-8,4,2])
vals.reverse()
for i in range(5):
     print(vals[i])

it will print:
5
9
-8
4
2


from array import *

vals = array('i',[5,9,-8,4,2])
vals.reverse()

for i in range(5):
     print(vals[i])

it will shows in just reverse format


create an array from user::

from array import *

arr = array('i', [])
n = int(input("Enter the range"))
for i in range(n):
    x = int(input("Enter the next num"))
    arr.append(x)
print(arr)
    
    
Take an input from user and create array and find the index number of a number::

from array import *

arr = array('i', [])
n = int(input("Enter the range"))
for i in range(n):
    x = int(input("Enter the next num"))
    arr.append(x)
print(arr)
    
val = int(input("Enter your search number"))

k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k=k+1
print(arr.index(val)) # Directly using function



write a code to sort the array in ascending order
write a code to find fractorial of a given number


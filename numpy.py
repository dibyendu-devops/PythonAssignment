from numpy import *
arr = array([1,2,4,2,3,4])
   
print(arr)

output will shows as below::

[6 7 9 7 8 9]


from numpy import *
arr = array([1,2,4,2,3,4])
print(sum(arr))

16

from numpy import *
arr = array([0, 30, 45, 60])
print(sin(arr))

from numpy import *
arr = array([0, 30, 45, 60])
print(max(arr))

from numpy import *
arr = array([0, 30, 45, 60, 35, 50])
print(sort(arr))

how to copy array:

from numpy import *
#arr = array([0, 30, 45, 60, 35, 50])
#print(sort(arr))

arr1 = array([2, 5, 6, 8])
arr2=arr1.view()
print(arr1,arr2)
print(id(arr1))
print(id(arr2))
with the view the id will be different and without view it will be same

## if you wish to copy the arrays but later you want to change the value of one of the array.
## Shallow copy - it will change for second array as well.
## Deep Copy - it will not change the value for second array


from numpy import *
#arr = array([0, 30, 45, 60, 35, 50])
#print(sort(arr))

arr1 = array([2, 5, 6, 8])
arr2=arr1.copy()
arr1[2]=7
print(arr1,arr2)

print(id(arr1))
print(id(arr2))

## in Output the value will be changed to 7 



########################write a code to add 2 arrays using for loop###############################


write a code to find the maxium value from an array without using in-build function


from numpy import *
arr1 = array([
              [1, 2, 3],
              [4, 5, 6]
            ])
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
arr2 = arr1.flatten()
print(arr2)

##### Convert 2 dimentional to 3,

from numpy import *
arr1 = array([
              [1, 2, 3, 4, 5, 6],
              [4, 5, 6, 7, 8, 9]
            ])

arr2 = arr1.flatten()
arr3 = arr2.reshape(3,4)
print(arr3)


MATRICES


from numpy import *
arr1 = array([
              [1, 2, 3, 4],
              [4, 5, 6, 7]
            ])

m = matrix(arr1)
print(m)


from numpy import *
m = matrix('1 2 3; 4 5 6; 7 8 9')
print(m)

[[1 2 3]
 [4 5 6]
 [7 8 9]]


from numpy import *
m = matrix('1 2 3; 4 5 6; 7 8 9')
print(diagonal(m))

[1 5 9]

from numpy import *
m = matrix('1 2 3; 4 5 6; 7 8 9')
print(m.max())

9

from numpy import *
m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('9 8 7; 6 5 4; 3 2 1')
m3 = m1 * m2;
print(m3)

[[ 30  24  18]
 [ 84  69  54]
 [138 114  90]]







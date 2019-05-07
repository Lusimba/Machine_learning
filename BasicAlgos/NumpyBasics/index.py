import numpy as np

a = np.array([[1, 2, 3],[2,3,4 ]])
print(type(a))

b = np.random.random(100)
print (b) # range array

print(np.ones((2,3))) # returns '1' array of size (2,3)

print(np.zeros((4,5))) #zero array of size 4x5
print(np.eye(3)) # identity matrix

print(np.full((3,3),7)) # Array of constants

print(np.linspace(0,10,11)) # (starting, ending, number of steps)
print(np.empty((2,2))) #empty array, displays garbage values
print(np.array([1,3,4], dtype=complex, ndmin=3))# 3-dimensional complex type array
print(np.dtype('i4')) #int32

            #Functions

#reshape
a = np.array([[1,2,3],[4,5,6]])
print(a.reshape(3,2))

#size of each item in bytes
print(a.itemsize)

#Number of dimensions
print(a.ndim)

#a as a 1-byte, 8-bit element array
a = np.array([[1,2,3],[4,5,6]], dtype=np.int8)
print(a.itemsize)

print(a[:2,1:3])


a=np.array([[1,2],[3,4]])
print(np.array([1,3,2]).T)
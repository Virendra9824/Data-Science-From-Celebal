print("\n#################################################\n")
heading = "Basics of NumPy"
print(heading.center(50, ' '))

import numpy as np

print(np.__version__)

arr = np.array([1,2,3,4])
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.size)
print(arr.itemsize)
print(arr)






print("\n#################################################\n")
heading = "Broadcasting"
print(heading.center(50, ' '))

arr2 = 10*arr
print(arr2)


arr3 = arr + np.array([100])
print(arr3)





print("\n#################################################\n")
heading = "Dot Product using List"
print(heading.center(50, ' '))

l1 = [1,2,3,4,5]
l2 = [5,4,3,2,1]

totalSum = 0
for i in range(0, len(l1)):
    totalSum += l1[i]*l2[i]

print(totalSum)





print("\n#################################################\n")
heading = "Dot Product using Array"
print(heading.center(50, ' '))

a1 = np.array(l1)
a2 = np.array(l2)
print(np.dot(a1,a2))





print("\n#################################################\n")
heading = "Speed Comparison of List & Array\n"
print(heading.center(50, ' '))

from timeit import default_timer as timer

T = 1000

a1 = np.random.randn(1000)
a2 = np.random.randn(1000)

l1 = list(a1)
l2 = list(a2)

def dot1():
    totalSum = 0
    for i in range(0, len(l1)):
        totalSum += l1[i]*l2[i]
    return totalSum

def dot2():
    ans = np.dot(a1,a2)
    return ans

start = timer()
for t in range(T):
    dot1()
end = timer()
t1 = end-start

start = timer()
for t in range(T):
    dot2()
end = timer()
t2 = end-start


print("List time: ", t1)
print("Array time: ", t2)
print("Ratio: ", t1/t2)





print("\n#################################################\n")
heading = "Random Number Generation\n"
print(heading.center(50, ' '))

print("Using np.random.rand(3,3):")
a1 = np.random.rand(3,3)
print(a1)

print("\nUsing np.random.randint(2,9,10):")
a1 = np.random.randint(2,9,10)
print(a1)

print("\nUsing np.random.randn(3,3):")
a1 = np.random.randn(3,3)
print(a1)





print("\n#################################################\n")
heading = "range vs arange\n"
print(heading.center(50, ' '))

lst = [*range(11,20,1)]
print(lst)


arr = np.arange(0,21,5)
print(arr)





print("\n#################################################\n")
heading = "Multidimensional Array\n"
print(heading.center(50, ' '))

arr = np.array([[1,2,3],
                [4,50,6],
                [7,8,9]])

print(arr.ndim)
print(arr.T)

print("Determinant of Matrix: ", np.linalg.det(arr))

print("Inverse of matrix: \n",np.linalg.inv(arr))

c = np.diag(arr)
print(c)
print(np.diag(c))




print("\n#################################################\n")
heading = "Slicing\n"
print(heading.center(50, ' '))


arr = np.random.randint(1,50, (4,4))
print("\nMatrix is: \n", arr)

print()
print(arr[1:,1:])

print()
print(arr[:,1:3])

print()
print(arr[1:3,1:3])

print()
print(arr[::-1,::])

print()
print(arr[::,::-1])

print()
bool_idx = arr > 25
print(bool_idx)
print(arr[bool_idx])

print()
print(np.where(arr>25, arr, -111))




print("\n#################################################\n")
heading = "Fancy Indexing\n"
print(heading.center(50, ' '))

arr = np.array([100,101,102,103,104,105])
fancyIdx = [3,4,5]
print(arr[fancyIdx])




print("\n#################################################\n")
heading = "Reshaping\n"
print(heading.center(50, ' '))

arr = np.arange(1,10)
print(arr)
print(arr.shape)
b = arr.reshape((3,3))
print(b)




print("\n#################################################\n")
heading = "hstack and vstack\n"
print(heading.center(50, ' '))

a = np.arange(1,4)
b = np.arange(5,8)
print(a)
print(b)

print()
h = np.hstack((a,b))
print(h)

print()
v = np.vstack((a,b))
print(v)




print("\n#################################################\n")
heading = "Eigen values and Eigen Vectors\n"
print(heading.center(50, ' '))


a = np.array([[1,2], [3,4]])
eignevalues, eigenvectors = np.linalg.eig(a)
print("eignevalues\n", eignevalues)

print("\neigenvectors\n", eigenvectors)
print()

# e_vec * e_val = A * e_vec
b = eigenvectors[:,0] * eignevalues[0]
print(b)

c = a @ eigenvectors[:,0]
print(np.allclose(b,c))




print("\n#################################################\n")
heading = "@ VS *\n"
print(heading.center(50, ' '))

arr1 = np.array([1,2])
arr2 = np.array([3,0])

print("arr1 * arr2: ", arr1 * arr2) # --> product of corresponding elements
print("arr1 @ arr2: ", arr1 @ arr2) # --> Matrix multiplication of array





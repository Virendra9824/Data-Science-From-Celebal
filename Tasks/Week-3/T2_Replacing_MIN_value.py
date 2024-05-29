'''
Task-2
Create a NumPy programme that generates a 5x5 array with
randomly assigned values and then replaces the minimum value
in the array with 0. 

'''

import numpy as np

arr = np.random.randint(-2,10, size=(5,5))
print("\n5*5 matrix with Random numbers is: \n", arr)


minValue = np.min(arr)
print("\nMinimum value in above matrix is: ", minValue)


arr = np.where(arr==minValue, 0, arr)

print("\nArray after replacing minValue with 0 is: \n", arr)







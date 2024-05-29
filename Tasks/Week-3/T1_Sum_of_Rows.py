'''
Task-1
Develop a NumPy program that generates a 4x4 array of random
values and calculates the sum of each row. 
'''

import numpy as np

arr = np.random.randint(1,100, size=(4,4))
print("\n4*4 matrix with Random numbers is: \n", arr)

rowSum = np.sum(arr,axis=1)
# print(rowSum)

print()
for i in range (0,len(rowSum)):
    print(f"Sum of row {i+1} is: ", rowSum[i])
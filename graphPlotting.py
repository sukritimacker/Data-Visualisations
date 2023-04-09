'''
Q1. Given two integer arrays, X and Y. Plot the graph between X and Y. Please consider.
x = np.array([0,1,2,3,4,5,6,7,9,10])
y=np.array([1,2,5,10,17,26,37,50,82,101])
From the help of graph, determine the range of Y when the value of X is 8.
Plot and print the range of Y.
Note: Here lower limit and upper limit of range must be multiple of 10 and difference between upper limit and lower limit must be equal to 10.


Output Format
lower_limit to upper_limit
'''

## Sol 1.
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,9,10])
y=np.array([1,2,5,10,17,26,37,50,82,101])

plt.plot(x,y)
plt.show()
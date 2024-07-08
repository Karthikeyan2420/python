# # NumPy is a Python library used for working with arrays.
# # It also has functions for working in domain of linear algebra, fourier transform, and matrices.
#
#
""" import numpy
arr = numpy.array([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr)
print(arr[1])
print(arr[2] + arr[3])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[0:10:2])   """

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
np.random.seed(42)
x = np.random.rand(50) * 10
y =  np.random.randn(50) * 10
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
plt.scatter(x, y, label='Data')
plt.plot(x, y_pred, color='red', label=f'Regression Line: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend() 
plt.show() 


""" import pandas as pd
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
print(mydataset)
myvar = pd.DataFrame(mydataset)
print(myvar) """
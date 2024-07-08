














# # Pandas is a Python library used for working with data sets.
# # It has functions for analyzing, cleaning, exploring, and manipulating data.
""" 
 """



import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

import pandas as p
a = [1, 7, 2]
myvar = p.Series(a, index=["x", "y", "z"])
print(myvar)  


""" import pandas as pd
#
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
print(mydataset)
myvar = pd.DataFrame(mydataset)
print(myvar) """
#
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
print(arr[1:10:2])  """


 

""" import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
a=[]
print(type(a))
print(type(arr)) """

""" 
import numpy as np
print(np.__version__)
#

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print('2nd element on 1st row: ', arr[0, 1]) """


""" import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0,2])
print("1. ",arr[1, 1:4])
print("2. ",arr[0:2, 2])
print("3. ",arr[0:2, 1:4]) """


# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7,8,9], [10,11,12]]])
# print("4.",arr)
# print("5. ",arr[0, 1, 2])









# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([0,3,5])
# ypoints = np.array([0,150,45])
# plt.plot(xpoints, ypoints)
# plt.show()   


# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(xpoints, ypoints)
# plt.title("title")
# plt.xlabel("number")
# plt.ylabel("mark")
# plt.show()   


# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoints)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# #plt.plot(ypoints, marker = 'o')
# plt.plot(ypoints, marker = '*')
# plt.show() 


# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, '*:g')
# #-,:,--,-.   red, green blue, cyan magenta, yellow, black as k, white
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 10)
# plt.show()
# #
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()
# #
# #
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.show()
# #
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, color = 'r')
# plt.show()
# plt.plot(ypoints, c = 'hotpink')
# plt.show()
# plt.plot(ypoints, linewidth = '20.5')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()
# #
# import matplotlib.pyplot as plt
# import numpy as np
# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(x1, y1, x2, y2)
# plt.show()

# #
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.plot(x, y)
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.show()
# #
# #
# #
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330]) 


font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(x, y)
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import linregress
# np.random.seed(42)
# x = np.random.rand(50) * 10
# y = 2 * x + 1 + np.random.randn(50) * 2
# slope, intercept, r_value, p_value, std_err = linregress(x, y)
# y_pred = slope * x + intercept
# plt.scatter(x, y, label='Data')
# plt.plot(x, y_pred, color='red', label=f'Regression Line: y = {slope:.2f}x + {intercept:.2f}')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
# plt.show() 



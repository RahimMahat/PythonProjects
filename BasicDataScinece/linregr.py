import numpy as np
import matplotlib.pyplot as plt

#  Linear Regression:

x = np.array([1,2,5,4,7,8,9,21,4,54,3,6,7])
y = np.array([10,12,16,14,17,18,19,31,6,33,15,7,27])
func1 = np.polyfit(x,y,1)

plt.plot(x,y,".")                           # x,y being co-ordinates and . for to get the graph in dot format
plt.plot(x,np.polyval(func1,x),"r-")        # to get linear regression line in the graph
plt.show()                                  # show the graph
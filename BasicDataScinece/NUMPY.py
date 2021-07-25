import numpy as np

#1D Array:
a1 = np.array([2,4,6,8,10])
print(a1)
#2D Array:
a2 = np.array([(1,3,5,7,9),(2,4,6,8,10)])
print(a2)
#Addition of 2D-array:
a3 = np.array([(1,5,9),(2,6,10)])
a4 = np.array([(3,7,9),(4,8,10)])
print(a3+a4)
#########################################################
ar1 = np.array([(2,6,10),(2,3,6)])

print(ar1.itemsize)         # checking item size
print(ar1.dtype)            # checking data type of elements in np array
print(ar1.ndim)             # checking dimension of array
print(ar1.size)             # checking size of array
print(ar1.shape)            # checking the shapee i.e (row,col)
ar1 = ar1.reshape(3,2)      # reshaping the arrazy i.e vice-versa
print(ar1.shape)
#############################################################
# linspace generateS numbers with equal spacing i.e (start_num, end_num, total_num)
arr1 = np.linspace(11,51,7)
print(arr1)

# 2D-array slicing
arr2 = np.array([(2,4,6),(1,3,5),(10,30,50),(11,32,53)])
print(arr2[0,1])
print(arr2[1:,1])

# max,min and sum
arr3 = np.array([(10,30,50),(11,32,53)])
print(arr3.max())
print(arr3.min())
print(arr3.sum())
#####################################################################
arra1 = np.array([(2,3,4),(5,3,7)])
arra2 = np.array([(2,9,1),(5,4,9)])

# 2d-array addition,substraction,multiplication,division
print(arra1+arra2)
print(arra1-arra2)
print(arra1*arra2)
print(arra1/arra2)

# putting all numbers in one column
print(arra1)
print(arra1.ravel())

#sum of axis
print(arra2.sum(axis=0))  # if axis=0 then sum of col. if axis=1 then sum of row

# square root:
print(np.sqrt(arra1))
# standard deviation:
print(np.std(arra2))
#######################################################################
array1 = np.array([2,3,4,5,1])
# Exponential
print(np.exp(array1))

# logarithmic
print(np.log(array1))
print(np.log10(array1))
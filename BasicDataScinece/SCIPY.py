from scipy import special
from scipy import integrate
import numpy as np
from scipy import linalg


var = special.kelvin(15)
print(var)

var1 = special.xlogy(2,10)
print(var1)

var2 = special.exp10(5)
print(var2)

var3 = special.sindg(90)
print(var3)
var4 = special.cosdg(90)
print(var4)



a = lambda x: x**3
# fun1 = integrate.quad(a,0,6)
# print(fun1)

b = lambda x,y: x*y**4
fun2 = integrate.dblquad(b,0,7,lambda x:0,lambda x:1)
print(fun2)




arr1 = np.array([(2,5),(6,7)])
arr2 = np.array([(1,4),(5,7)])

fun1 = linalg.solve(arr1,arr2)
print(fun1)
rvrs = linalg.inv(arr1)
print(rvrs)
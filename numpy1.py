import numpy as np

a = np.array([[1,2,-2],[2,-2,-1],[2,1,2]])
a1 = np.matrix(a)
b = np.diag([1,0,-1])
# print(a1)
# print(b)
d = a1*b
print(d)
c = a1.I *9
print(d*c/9)
import numpy as np
x=np.array([
    [2,1,3],
    [4,3,5],
    [7,3,8]
    
])
v= np.array([1,0,1])
# y=np.empty_like(x)
# print(y)
# for i in range(len(x)):
#     y[i, :]=x[i,:]+v
# print(y)
# stacked_v=np.tile(v,(3,1))
# print(stacked_v)
# print(x+stacked_v)
print(x+v)
y=np.array([
    [4,5,6],
    [1,2,4]
])
print(y)
print(y.shape)
z=np.reshape(y,(3,2))
print(z,z.shape)

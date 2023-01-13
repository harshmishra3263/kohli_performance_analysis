# # import numpy as np
# # arr=np.array([
# #     [2,3],
# #     [7,4]
# # ])
# # # print(arr)
# # # print(type(arr))
# # #    #numpy.ndarray
# # # #shape of an array
# # # print(arr.shape)

# # # print(arr[0],arr[1])
# # # arr[1]=10
# # # print(arr)
# # arr2D=np.array([
# #     [2,5,3],
# #     [1,6,8]
# # ])
# # # print(arr2D)
# # # print(arr2D.shape)

# # # print(arr2D[0],type(arr2D[0]))
# # # print(arr2D[1],type(arr2D[1]))

# # # print(arr2D[0,0],arr2D[0,1],arr2D[0,2],arr2D[1,0],arr2D[1,1],arr2D[1,2])
# # zeros=np.zeros((3,4))
# # print(zeros,type(zeros),zeros.shape)
# # ones= np.ones((4,5))
# # print(ones,ones.shape)
# import numpy as np
# consts=np.full((3,6),5)
# # print(consts,consts.shape)
# # print(consts,consts.shape)
# # random=np.random.random((4,5))
# # print(random,random.shape)

# n=int(input("Enter the number:"))
# for i in range(0,n):
#     for j in range(0,n):
#         if i==j:
#             consts[i,j]=0

       
# print(consts)
import numpy as np
# temp=np.array([
#      [5,6,7,1],
#      [3,5,7,8],
#      [2,5,7,1]
# ])
# print(temp)

# s_arr=temp[:2, 1:3]
# print(s_arr)
# s1_arr=temp[1:,2:]
# print(s1_arr)
# s2_arr=temp[1,:]
# print(s2_arr)

# print(temp>2)
# print(temp[temp>2])
# x=np.array([[3,4,8],[3,6,0]],dtype=np.float64)
# print(x)
# print(x.dtype)

# y=np.array([[5,4,6],[2,4,5]],dtype=np.float64)
# print(y,y.dtype)
# print(x+y)
# print(np.add(x,y))
# print(np.divide(x,y))

# x=np.array([[3,4,8],[3,6,0]],dtype=np.float64)
# y=np.array([[5,4,6],[2,4,5]],dtype=np.float64)
# v=np.array([9,10],dtype=np.float64)
# w=np.array([5,6])
# print(v.dot(w))
# print(np.dot(v,w))
#print(x.dot(v))
# print(np.dot(x,v))
u=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(u)
print(u.T)
print(u*(u.T))
print(np.sum(u))
print(np.sum(u,axis=0))
print(np.sum(u,axis=1))

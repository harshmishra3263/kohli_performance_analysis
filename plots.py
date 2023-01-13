import numpy as np

import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)
# plt.plot(x,y_sin)
# plt.plot(x,y_cos)

# plt.xlabel("X axis level")
# plt.ylabel("Y axis level")
# plt.title("Sine and Cosine")
# plt.legend(["Sine","Cosine"])
# plt.show()

#creating the first plot
# plt.subplot(2,1,1)
# plt.plot(x,y_sin)
# plt.title("Sine wave")

#creating the second plot
# plt.subplot(2,1,2)
# plt.plot(x,y_cos)
# plt.title("Cosine wave")
# plt.show()

#parabola
#x=np.arange(-3*np.pi,3*np.pi,0.1)
x=np.linspace(-20,20,100)
def func(x):
    y=[]
    for elem in x:
        #result=5*(elem**2)+6*elem+3
        result=1-(elem*elem)/2
        y.append(result)
    return y
y=func(x)
# y_sin=x**2*np.sin(x)*np.sin(x)
# y_cos=x**2*np.cos(x)*np.cos(x)
# y=x**2
# plt.plot(x,y)
#y=5*(x**2) +6*x+3
plt.plot(x,y)

# plt.plot(x,y_sin)
# plt.plot(x,y_cos)
plt.show()
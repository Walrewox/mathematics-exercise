import numpy as np
import matplotlib.pyplot as plt

y = lambda x: np.sin(x**3)-x**2

def searchMax(a,b,step):
    while abs(a-b) >= step:
        if y(a) < y(b):
            a = (a+b)/2
        else:
            b = (a+b)/2
    return (a+b)/2

start = -5
end = 5
step = .01
x = np.arange(start,end,step)

max = searchMax(start,end,step)

plt.figure("Searching of maximum and minimum value of function")
plt.title("Dichotomy method")
plt.plot(x,y(x), label = "Графік функції")
plt.scatter(max,y(max), c = "red", label = "Максимум на інтервалі")
plt.grid()
plt.legend(loc = "best")
plt.show()

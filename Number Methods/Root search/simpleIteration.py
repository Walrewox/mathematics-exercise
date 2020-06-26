# Python implementation of Simple fixed-point Iteration method for root search #
import numpy as np
import matplotlib.pyplot as plt

y = lambda x: np.sin(x)
def SFPI(x,step):
    r = []
    i = 1
    for i in x:
        if((y(i-step)*y(i)) < 0):
            r.append(((i-step)+i)/2)
    if r == 0:
        print("Root not found in this interval or it's equal zero!")
    return r
start = -10
end = 10
step = .01
x = np.arange(start,end,step)
roots = SFPI(x,step)

plt.figure("Simple iteration method")
plt.title("Roots of sine wave on interval between -10 and 10")
plt.plot(x, y(x), label = "Graph of function")
plt.scatter(roots, y(roots), label = "Roots of function", marker = "o", c = "red")
plt.legend(loc = "best")
plt.grid(b = True)
plt.show()

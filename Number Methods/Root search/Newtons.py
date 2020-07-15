# Python implementation of Newton's method for root search #
import numpy as np
import matplotlib.pyplot as plt

plt.figure("Newton's method")

f = lambda x: np.sin(x)-x*2
df = lambda x: np.cos(x)-2
tangent = lambda x: x*df(x)
def Newton(a,b,eps):
    lines = 0
    if (f(a) * df(a) > 0):
        x0 = a
    else:
        x0 = b
    xn = x0 - f(x0) / df(x0)
    while abs(x0 - xn) > eps:
        lines += 1
        x0 = xn
        xn = x0 - f(x0) / df(x0)
        line = np.arange(xn-3,xn+3,eps)
        plt.plot(line,tangent(line), label = f"{lines} iteration")
    root = (x0+xn)/2
    return root
start = -10
end = 5
step = .001
plt.title(f"Root of sine wave on interval between {start} and {end}")

x = np.arange(start,end,step)
root = Newton(start,end,step)


plt.plot(x, f(x), label = "Graph of function")
plt.scatter(root, f(root), label = "Root of function", marker = "o", c = "red")
plt.legend(loc = "best")
plt.grid(b = True)
plt.show()

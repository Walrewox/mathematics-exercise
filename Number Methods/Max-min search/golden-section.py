import numpy as np
import matplotlib.pyplot as plt

y = lambda x: np.sin(x**3)-x**2
F = 1.618 #golden ratio

def search(a,b,eps):
    while abs(b-a) > eps:
        print(b-a)
        x1 = b-((b-a)/F)
        x2 = a+((b-a)/F)
        if y(x1) < y(x2): #for search maxima or minima - reverse the symbol
            a = x1
        else:
            b = x2
    return (a+b)/2

start = -5
end = 3
step = .01
x = np.arange(start,end,step)

result = search(start,end,step)

plt.figure("Searching of maximum and minimum value of function")
plt.title("Golden section search")
plt.plot(x,y(x), label = "Graph of function")
plt.scatter(result,y(result), c = "red", label = "Result")
plt.grid()
plt.legend(loc = "best")
plt.show()

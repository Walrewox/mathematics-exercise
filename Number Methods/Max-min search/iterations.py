import numpy as np
import matplotlib.pyplot as plt

y = lambda x: x**2+np.log(42**np.sin(x))

def search(x):
    max = x[0]
    min = x[0]
    for i in x:
        if y(i) < y(min):
            min = i
        if y(i) > y(max):
            max = i
    result = [max,min]
    return result

start = -10
end = 10
x = np.arange(start,end,.1)
scatters = search(x)

plt.figure("Searching of maximum and minimum value of function")
plt.title("Iterations method")
plt.plot(x,y(x), label = "Графік функції")
plt.scatter(scatters[0],y(scatters[0]), c = "red", label = "Максимум на інтервалі")
plt.scatter(scatters[1],y(scatters[1]), c = "blue",label = "Мінімум на інтервалі")
plt.grid()
plt.legend(loc = "best")
plt.show()

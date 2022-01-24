from math import sin, sqrt
import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import curve_fit

Weight = [ (1, 67.3),  (2,67.1),  (4,66.4),  (8,65.7), (10, 64.9),
           (11, 65.3), (13,63.9), (14,64.1), (18,64.7), (20, 64.1),
           (25, 64.5), (26,63.4), (27,63.6), (31,62.7), (32, 62.5)
         ]

day = []
weight = []
for w in Weight :
    day.append(w[0])
    weight.append(w[1])
day = np.array(day)

def func_1(x, a, b, c, d):
    return a * x + np.sin(b * x)  + c
    #return a * x * x * x + b * x * x + c * x + d

plt.scatter(day, weight, color='r', label="1")
result_x, result_y = curve_fit(func_1, day, weight)
plt.plot(day, func_1(day, *result_x), label="fitting1")
#print("y=" + str(result_x[0]) + " x+ " + str(result_x[1]))
plt.legend()
plt.show()


print(func_1(50, *result_x))
print(func_1(100, *result_x))
print(func_1(200, *result_x))

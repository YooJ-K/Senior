from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import curve_fit

def func_1(X, a, b):
    return a * X + b

def func_2(X, a, b, c):
    return a * pow(X-b, 2) + c

def func_3(X, a, b):
    return a * X * X + b

x1 = np.array([5, 11, 15, 44, 60, 70, 75, 100, 120, 200])
y1 = [2.492, 8.330, 11.000, 19.394, 24.466, 27.777, 29.878, 26.952, 35.607, 46.966]

x2 = np.array([5,6,7,9,13,15,21,25,32,33])
y2 = [177,196,204,230,248,264,249,238,172,153]

x3 = np.array([5, 11, 12, 17, 26, 37, 45, 60, 70, 72])
y3 = [2.800, 1.500, 2.450, 3.200, 27.450, 48.800, 64.200, 141.450, 201.450, 226.050]

plt.scatter(x1, y1, color='r', label="1")
result_x, result_y = curve_fit(func_1, x1, y1)
plt.plot(x1, func_1(x1, *result_x), label="fitting1")
print("y=" + str(result_x[0]) + " x+ " + str(result_x[1]))
plt.legend()
plt.show()

plt.scatter(x2, y2, color='r', label="2")
result_x, result_y = curve_fit(func_2, x2, y2)
plt.plot(x2, func_2(x2, *result_x), label="fitting2")
print("y=" + str(result_x[0]) + " * ( x - " + str(result_x[1]) + ") ^ 2 + " + str(result_x[2]))
plt.legend()
plt.show()

plt.scatter(x3, y3, color='r', label="3")
result_x, result_y = curve_fit(func_3, x3, y3)
plt.plot(x3, func_3(x3, *result_x), label="fitting3")
print("y=" + str(result_x[0]) + " * x^2 " + str(result_x[1]))
plt.legend()
plt.show()
import numpy
import scipy.optimize as optimization
import matplotlib.pyplot as plt

xdata = numpy.array([0.0,1.0,2.0,3.0,4.0,5.0])
ydata = numpy.array([0.1,0.9,2.2,2.8,3.9,5.1])

x0    = numpy.array([0.0, 0.0, 0.0])
sigma = numpy.array([1.0,1.0,1.0,1.0,1.0,1.0])

def func(x, a, b, c):
    return a + b*x + c*x*x

print(optimization.curve_fit(func, xdata, ydata, x0, sigma))



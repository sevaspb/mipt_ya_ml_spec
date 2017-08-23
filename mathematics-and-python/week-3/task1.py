import numpy
import pylab

from IPython.display import display, Markdown
from scipy.optimize import minimize
from functions import fun, print_fun, numpy_fun

display(Markdown('# Задача 1. Минимизация гладкой функции методом градиентного спуска'))

print_fun();

display(Markdown('Исследуем функцию на интервале [1, 30]'))

for x0 in range(1, 31):
  result = minimize(fun, x0, method='BFGS')
  print(f"Результат при x0={x0}: x={result.x} fun={result.fun} nfev={result.nfev}")

display(Markdown('График исследуемой фукнции на интервале [1, 30]'))
x = numpy.linspace(0, 30, 100)
pylab.plot(x, numpy_fun(x))
pylab.show()


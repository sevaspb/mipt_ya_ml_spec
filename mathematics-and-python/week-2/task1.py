import numpy
import pylab

from IPython.display import display, Markdown
from scipy.optimize import minimize
from math import sin, exp

display(Markdown('# Задача 1. Минимизация гладкой функции методом градиентного спуска'))

display(Markdown('$$\\sin(\\frac{x}{5}) * \\exp(\\frac{x}{10}) + 5*\\exp(\\frac{-x}{2})$$'))
def function(x):
  return sin(x/5) * exp(x/10) + 5*exp(-x/2)

display(Markdown('Исследуем функцию на интервале [1, 30]'))

for x0 in range(1, 31):
  result = minimize(function, x0, method='BFGS')
  print(f"Результат при x0={x0}: x={result.x} fun={result.fun} nfev={result.nfev}")

display(Markdown('График исследуемой фукнции на интервале [1, 30]'))
x = numpy.linspace(0,30,100)
y = numpy.sin(x/5) * numpy.exp(x/10) + 5*numpy.exp(-x/2)
pylab.plot(x, y)
pylab.show()


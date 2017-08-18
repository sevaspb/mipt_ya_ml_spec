import numpy
import pylab

from IPython.display import display, Markdown
from scipy.optimize import differential_evolution
from math import sin, exp

display(Markdown('# Задача 2. Минимизация гладкой функции методом DE (дифференциальной эволюции)'))

display(Markdown('$$\\sin(\\frac{x}{5}) * \\exp(\\frac{x}{10}) + 5*\\exp(\\frac{-x}{2})$$'))
def function(x):
  return sin(x/5) * exp(x/10) + 5*exp(-x/2)

display(Markdown('Исследуем функцию на интервале [1, 30]'))
bounds = [(1, 30)]
result = differential_evolution(function, bounds)
print(f"Результат: x={result.x}, fun={result.fun} nfev={result.nfev}")


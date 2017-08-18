import numpy
import pylab

from IPython.display import display, Markdown
from scipy.optimize import minimize
from math import sin, exp

display(Markdown('# Задача 3. Минимизация негладкой функции'))

display(Markdown('$$f(x)=\\sin(\\frac{x}{5}) * \\exp(\\frac{x}{10}) + 5*\\exp(\\frac{-x}{2})$$'))
display(Markdown('$$h(x)=int(f(x))$$'))

def f(x):
  return sin(x/5) * exp(x/10) + 5*exp(-x/2)

def h(x):
  return int(f(x))

display(Markdown('## Исследуем функцию на интервале [1, 30] методом градиентного спуска'))
for x0 in range(1, 31):
  result = minimize(h, x0, method='BFGS')
  print(f"Результат при x0={x0}: x={result.x} fun={result.fun} nfev={result.nfev}")

display(Markdown('## Поиск глобального минимума на [1, 30] методом DE'))
bounds = [(1, 30)]
result = differential_evolution(h, bounds)
print(f"Результат: x={result.x}, fun={result.fun} nfev={result.nfev}")

display(Markdown('## График исследуемой фукнции на интервале [1, 30]'))
x = numpy.linspace(0,30,100)
y = numpy.round(numpy.sin(x/5) * numpy.exp(x/10) + 5*numpy.exp(-x/2))
pylab.plot(x, y)
pylab.show()


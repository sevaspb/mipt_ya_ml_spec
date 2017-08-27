from IPython.display import display, Markdown
import numpy as np
import pylab
import scipy
from math import sin, exp

def fun(x):
  return sin(x/5) * exp(x/10) + 5*exp(-x/2)

def numpy_fun(x):
  return np.sin(x/5) * np.exp(x/10) + 5*np.exp(-x/2)

# A = [
#   [x[0]**0, x[0]**1, ... x[0]**n],
#   [x[1]**0, x[1]**1, ... x[1]**n],
#   ...
#   [x[n]**0, x[n]**1, ... x[n]**n]
#]
def build_A(x):
  size = len(x)
  return list(map(lambda item:
    list(map(lambda i: pow(item, i), range(size)))
    ,x)
  )

# b = [fun(x[0]), fun(x[1]), ... fun(x[n])]
def build_b(x):
  return list(map(lambda item: fun(item), x))

def solve(x):
  A = build_A(x)
  b = build_b(x)
  w = scipy.linalg.solve(A, b)
  return [A, b, w]

# Нужно переставить элементы полученного результата
# посколько poly1d использует другой способ записи системы уравнения
# см https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html
def poly1d(w):
  return np.poly1d(list(reversed(w)))

_, _, w2 = solve([1, 15])
_, _, w3 = solve([1, 8, 15])
_, _, w4 = solve([1, 4, 10, 15])
display(Markdown('## Коэффиценты для системы четвёртой степени'))
print(w4)

display(Markdown('## График аппроксимации исследуемой функции'))
steps = np.linspace(0, 16, 100)
pylab.plot(steps, numpy_fun(steps), '-g',
           steps, poly1d(w2)(steps), '-',
           steps, poly1d(w3)(steps), '+',
           steps, poly1d(w4)(steps), '--')
pylab.legend(['Original function', '2th degree poly', '3th degree poly', '4th degree poly'])
pylab.show()

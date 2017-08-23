import numpy
import pylab

from IPython.display import display, Markdown
from scipy.optimize import differential_evolution
from functions import fun, print_fun

display(Markdown('# Задача 2. Минимизация гладкой функции методом DE (дифференциальной эволюции)'))

print_fun()

display(Markdown('Исследуем функцию на интервале [1, 30]'))
bounds = [(1, 30)]
result = differential_evolution(fun, bounds)
print(f"Результат: x={result.x}, fun={result.fun} nfev={result.nfev}")


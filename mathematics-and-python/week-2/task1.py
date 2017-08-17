from IPython.display import display, Markdown
from scipy.optimize import minimize
from math import sin, exp

display(Markdown('# Задача 1. Минимизация гладкой функции'))

display(Markdown('$$\\sin(\\frac{x}{5}) * \\exp(\\frac{x}{10}) + 5*\\exp(\\frac{-x}{2})$$'))
def function(x):
  return sin(x/5) * exp(x/10) + 5*exp(-x/2)

interval = [1, 30]

print f"Первый запуск: {minimize(function, interval)}"


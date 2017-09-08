import pandas as pd
import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt
import math

from IPython.display import display, Markdown
from scipy.stats import pareto

def plot(rv, hist_vars, rv_label, hist_label):
  _, ax = plt.subplots(1, 1)
  # Генерирует числа для графика
  x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 10)
  # Рисуем функцию плотности для непрерывного распределения rv
  ax.plot(x, rv.pdf(x), 'r-', lw=3, alpha=0.6, label=rv_label)
  # Рисуем гистограмму по hist_vars
  ax.hist(hist_vars, normed=True, histtype='stepfilled', alpha=0.2, label=hist_label)

display(Markdown('# Распределение Парето'))
b = 128
pareto_rv = sts.pareto(b)
display(Markdown(f"## Коэффицент распеределения b={b}"))

plot(pareto_rv, pareto_rv.rvs(1000), 'Pareto pdf', 'Histogram')

def build_vars(n, size):
  return [calculate_E(pareto_rv.rvs(n)) for _ in range(size)]

def calculate_E(vars):
  return np.sum(vars) / np.size(vars)

def mean():
  return pareto_rv.mean()

def std(n):
  return math.sqrt(pareto_rv.var() / n)

def plot_gist(n, size, plt):
  _, ax = plt.subplots(1, 1)
  norm_rv = sts.norm(mean(), std(n))
  x = np.linspace(norm_rv.ppf(0.01),
                  norm_rv.ppf(0.99), 10)
  ax.plot(x, norm_rv.pdf(x), 'r-', lw=3, alpha=0.6, label='Norm pdf')
  ax.hist(build_vars(n, size), normed=True, histtype='stepfilled', alpha=0.2, label=f"n={n}")

  ax.legend(loc='best', frameon=False)

for n in [5, 10, 50]:
  plot_gist(n, 1000, plt)
plt.show()

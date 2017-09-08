import pandas as pd
import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt
import math
from IPython.display import display, Markdown

class SampleMean():
  # Инициируем наш класс с функцией распределения и размером выборки
  def __init__(self, rv, n):
    self.rv = rv
    self.n = n

  # Возвращает массив длинной size состоящий из выборочных средних
  def hist_vars(self, size):
    return [self.__mean(self.rv.rvs(self.n)) for _ in range(size)]

  # Возвращает мат.ожидание для апроксимирующего нормального распределения (согласно ЦПТ)
  def norm_mean(self):
    return self.rv.mean()

  # Возвращает стандартное отклонение для апроксимирующего нормального распределения (согласно ЦПТ)
  def norm_std(self):
    return math.sqrt(self.rv.var() / self.n)

  # Выборочное среднее. Сумма всех элементов поделенное на колво
  def __mean(self, vars):
    return np.sum(vars) / np.size(vars)

# Функция отрисовки результатов
def plot(rv, hist_vars, rv_label, hist_label):
  _, ax = plt.subplots(1, 1)
  # Генерирует числа для графика
  x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 10)
  # Рисуем функцию плотности для непрерывного распределения rv
  ax.plot(x, rv.pdf(x), 'r-', lw=3, alpha=0.6, label=rv_label)
  # Рисуем гистограмму по hist_vars
  ax.hist(hist_vars, normed=True, histtype='stepfilled', alpha=0.2, label=hist_label)
  ax.legend(loc='best', frameon=False)
  ax.set_ylabel('$f(x)$')
  ax.set_xlabel('$x$')

################
# Основной код #
################

display(Markdown('# Распределение Парето'))
b = 128
pareto_rv = sts.pareto(b)
display(Markdown(f"## Коэффицент распеределения b={b}"))

plot(pareto_rv, pareto_rv.rvs(1000), 'Pareto pdf', 'Histogram')

for n in [5, 10, 50]:
  cls = SampleMean(pareto_rv, n)
  plot(
    sts.norm(cls.norm_mean(), cls.norm_std()),
    cls.hist_vars(1000),
    "Norm pdf",
    f"n={n}"
  )

plt.show()

display(Markdown("При увеличении n становится всё более нагляна центральная предельная теорема. График плотности нормально распределения, постороенный на статистиках исходного распределения Парето, лучше аппроксимирует гистограмму, построенную по выборочному среднему."))

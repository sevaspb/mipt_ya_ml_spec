import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import display, Markdown
from scipy.stats import pareto

display(Markdown('# Распределение Парето'))
b = 3.14
display(Markdown(f"## Коэффицент распеределения b={b}"))
fig, ax = plt.subplots(1, 1)

# Генерирует числа для графика
x = np.linspace(pareto.ppf(0.01, b),
                pareto.ppf(0.99, b), 100)

# Рисуем функцию плотности для нашего распределения
ax.plot(x, pareto.pdf(x, b), 'r-', lw=3, alpha=0.6, label='Pareto pdf')

# Делаем выборку 1000 значений по нашей фукнции
r = pareto.rvs(b, size=1000)

# Рисуем гистограмму

ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()


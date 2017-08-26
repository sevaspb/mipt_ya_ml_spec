import os
import re
import itertools
import numpy as np
from collections import Counter

def read_file(name):
  dir_path = os.path.dirname(os.path.realpath(__file__))
  file = open(os.path.join(dir_path, name))
  return file.readlines()

def uniq_terms(arr):
  flatten = itertools.chain.from_iterable(arr)
  uniq = set(flatten)
  return list(sorted(uniq))

class Line():
  def __init__(self, line):
    self.line = line
    self.gist = self.__to_gist(line)
    self.counter = Counter(self.gist)

  def weight(self, term):
    return self.counter[term]

  def __to_gist(self, line):
    arr = re.split('[^a-z]', line)
    return list(filter(None, arr))

lines = list(map(lambda line: Line(line), read_file("sentences.txt")))
terms = uniq_terms(map(lambda line: line.gist, lines))
weights = map(lambda line:
  list(map(lambda term: print(line.weight(term)), terms))
  ,lines)
print(np.array(list(weights)))
# строки токенизировать в массив
# массив почистить
# все уникальные слова - gist
# получить матрицу с вхождением слова в массив
# посчитать косинусное расстояние
# записать в файл?

import os
import re
import itertools

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

  def __to_gist(self, line):
    arr = re.split('[^a-z]', line)
    return list(filter(None, arr))

lines = map(lambda line: Line(line), read_file("sentences.txt"))
terms = uniq_terms(map(lambda line: line.gist, lines))
print(terms)
# строки токенизировать в массив
# массив почистить
# все уникальные слова - gist
# получить матрицу с вхождением слова в массив
# посчитать косинусное расстояние
# записать в файл?

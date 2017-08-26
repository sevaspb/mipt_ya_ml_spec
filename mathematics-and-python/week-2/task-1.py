import os
import re
import itertools
from IPython.display import display, Markdown
import numpy as np
from scipy.spatial.distance import cdist
from collections import Counter

class Line():
  def __init__(self, line):
    self.line = line
    self.gist = self.__to_gist(line)
    self.counter = Counter(self.gist)

  def weight(self, term):
    return self.counter[term]

  def __to_gist(self, line):
    arr = re.split('[^a-z]', line.lower())
    return list(filter(None, arr))

def read_file(name):
  dir_path = os.path.dirname(os.path.realpath(__file__))
  file = open(os.path.join(dir_path, name))
  return file.readlines()

def uniq_terms(arr):
  flatten = itertools.chain.from_iterable(arr)
  uniq = set(flatten)
  return list(sorted(uniq))

def get_results(dist, count):
  idx = dist.argsort()[:count]
  return [idx, dist[idx]]

lines = list(map(lambda line: Line(line), read_file("sentences.txt")))
terms = uniq_terms(map(lambda line: line.gist, lines))
weights = list(map(lambda line:
  list(map(lambda term: line.weight(term), terms))
  ,lines))
matrix = np.array(weights)
dist = cdist(matrix[0:1], matrix[1:], metric='cosine')
idx, values = get_results(dist[0], 2)

display(Markdown('# Косинусные расстояния м\у первым вектором и последующими'))
print(dist)
print("Самый схожие предложения (минимальное косинусное расстояние) %s на позициях %s" % (values, [1 + x for x in idx]))

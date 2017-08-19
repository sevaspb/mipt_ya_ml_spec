import numpy
from IPython.display import display, Markdown
from math import sin, exp

def fun(x):
  return sin(x/5) * exp(x/10) + 5*exp(-x/2)

def numpy_fun(x):
  return numpy.sin(x/5) * numpy.exp(x/10) + 5*numpy.exp(-x/2)

def print_fun():
  display(Markdown('$$fun(x)=\\sin(\\frac{x}{5}) * \\exp(\\frac{x}{10}) + 5*\\exp(\\frac{-x}{2})$$'))


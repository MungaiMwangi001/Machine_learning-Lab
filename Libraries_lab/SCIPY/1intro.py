'''
SciPy Introduction
What is SciPy?
SciPy is a scientific computation library that uses NumPy underneath.

SciPy stands for Scientific Python.

It provides more utility functions for optimization, stats and signal processing.

Like NumPy, SciPy is open source so we can use it freely.

SciPy was created by NumPy's creator Travis Olliphant.

Why Use SciPy?
If SciPy uses NumPy underneath, why can we not just use NumPy?

SciPy has optimized and added functions that are frequently used in NumPy and Data Science.

Which Language is SciPy Written in?
SciPy is predominantly written in Python, but a few segments are written in C.


'''


'''Import SciPy
Once SciPy is installed, import the SciPy module(s) you want to use in your applications by adding the from scipy import module statement:'''


from scipy import constants

print(constants.liter)


import scipy

print(scipy.__version__)
# -*- coding: utf-8 -*-
"""
Spyder Editor

Log graphs
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import functools
import itertools
numbers = np.arange(0.0001,1,0.00001)

y = np.log2(numbers)
sns.scatterplot(numbers,y)
plt.show()

y2 = map(lambda x: x*np.log2(x) ,numbers)
sns.scatterplot(numbers,y2)
plt.show()


y3 = map(lambda x: -1*x*np.log2(x) ,numbers)
sns.scatterplot(numbers,y3)
plt.show()


y4 = itertools.accumulate(map(lambda x: -1*x*np.log2(x) ,numbers),lambda x,y : x+y)
sns.scatterplot(numbers,y4)
plt.show()


def getEntropy(x):
    y = 1-x
    return -1*(x*np.log2(x) + y*np.log2(y))

entropy = map(getEntropy,numbers)
sns.scatterplot(numbers,entropy)
plt.show()


def getGini(x):
    y = 1-x
    return 1-(x*x + y*y)

gini = map(getGini,numbers)
sns.scatterplot(numbers,gini)
plt.show()



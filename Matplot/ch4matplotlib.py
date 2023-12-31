# -*- coding: utf-8 -*-
"""matplot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e2XZ45wSwUMrWNGi0WBa5PtmVnzXNosX
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

y = np.random.randint(0, 10, 10)
plt.plot(y, '+b-')

power = 1
for i in range(1, 3):
  for j in range(1, 3):
    a = [x ** power for x in range(-5, 6) ]
    y = np.array(a)
    x = np.array([x for x in range(-5, 6)])
    plt.subplot(2, 2, power)
    plt.plot(x, y)
    power += 1

"""Scatter plot"""

x = 4 + np.random.normal(0, 2, 50)
y = 4 + np.random.normal(0, 2, len(x))
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))
plt.scatter(x, y, c = colors, s = sizes)

"""Example - plotting various charts on a dataset"""

df = pd.read_csv('/USACities.csv')
df.head()

x = [i for i in range(0, 10)]
cities = df['name'][0:10]
y = df['pop2021'][0:10]
sizes = df['pop2010'][0:10]
sizes /= 10000
plt.xticks(x, cities)
plt.scatter(x, y, s = sizes)

x = df['density'][0:5]
labels = df['name'][0:5]
colors = plt.get_cmap('Greens')(np.linspace(0.2, 0.7, len(x)))
plt.pie(x, colors = colors, labels = labels, radius = 1.5,
        wedgeprops={"linewidth": 1, "edgecolor": "white"}, labeldistance = 0.5)

x = np.arange(10)
cities = df['name'][0:10]
y = df['pop2021'][0:10]
colors = plt.get_cmap('gray_r')(np.linspace(0.2, 0.7, len(x)))
plt.xticks(x, cities)
plt.bar(x, y, edgecolor = 'white', width = 1, color = colors)
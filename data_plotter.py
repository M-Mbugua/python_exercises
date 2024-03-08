# Please plot the data of 'data_points.txt' into a graph of x and y-axis.

import pandas, matplotlib.pyplot as plt

data_points = pandas.read_csv('data_points.txt')

data_points.plot(kind = 'scatter', x = 'x', y = 'y')

plt.show()


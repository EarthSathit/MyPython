import numpy as np
from decimal import Decimal
from scipy import stats
import math
import matplotlib.pyplot as plt

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
"""
x = np.mean(speed)
y = np.median(speed)
z = stats.mode(speed)
"""
# per = np.percentile(ages, 75)
data_set = np.random.uniform(0.0, 5.0, 1000000)
"""
print('%.2f' % x)
# print(round(Decimal(x), 2))
print('%.2f' % y)
print(z)
print(per)
"""
print(data_set)
plt.hist(data_set, 100)
plt.show()


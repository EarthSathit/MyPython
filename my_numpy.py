import numpy as np
from decimal import Decimal
from scipy import stats
import math

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = np.mean(speed)
y = np.median(speed)
z = stats.mode(speed)
print('%.2f' % x)
# print(round(Decimal(x), 2))
print('%.2f' % y)
print(z)

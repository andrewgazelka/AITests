import math
import random
from tkinter import Tk

import matplotlib.pyplot as plt

point_num = 20
max_x = 100
max_y = 100

points = [(random.random()*max_x, random.random()*max_y) for i in range(point_num)]


# window = Tk()

def distance2(point_list: list):
    dist2_sum = 0
    for i in range(len(points) - 1):
        a = points[i]
        b = points[i + 1]
        dist2_sum += point_distance2(a, b)
    dist2_sum += point_distance2(point_list[-1], point_list[0])
    return dist2_sum


def point_distance2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


temp = 1
temp_threshold = 0.1
current = -4_000


while temp > temp_threshold:
    idx = range(len(points))
    i1, i2 = random.sample(idx, 2)
    points_copied = points.copy()
    points_copied[i1], points_copied[i2] = points_copied[i2], points_copied[i1]
    result = -distance2(points_copied)
    exponent = result - current
    value = math.e ** (exponent / temp)
    if value > random.random():
        current = result
        points = points_copied
    temp -= temp_threshold


x = list(map(lambda x: x[0], points))
y = list(map(lambda x: x[1], points))

plt.scatter(x, y)
plt.plot(x, y)
plt.grid(True)

plt.show()
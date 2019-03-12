import math
import random
from tkinter import Tk, Canvas, Button

point_num = 20
max_x = 300
max_y = 300

points = [(random.random() * max_x, random.random() * max_y) for i in range(point_num)]


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


temp = 1_000_000
temp_multiplier = .98
current = -1E10

root = Tk()
root.title("Title")
root.geometry("100x100")

c = Canvas(root, width=max_x, height=max_y)
c.pack()
# c.pack()

count = 0


def on_click():
    global temp
    global points
    global current
    if temp > temp_multiplier:
        c.delete("all")
        idx = range(len(points))
        i1, i2 = random.sample(idx, 2)
        points_copied = points.copy()
        points_copied[i1], points_copied[i2] = points_copied[i2], points_copied[i1]
        result = -distance2(points_copied)
        exponent = result - current

        probability_accept = 1.0 if exponent > 0 else math.e ** (exponent / temp)

        if probability_accept > random.random():
            print("accepted", probability_accept)
            current = result
            points = points_copied
        else:
            print("denied:", probability_accept)
            print("old: ", current, "new: ", result)

        print("temp:",temp)

        for i in range(len(points) - 1):
            c.create_line(3*points[i], 3*points[i + 1])
        c.create_line(3*points[-1], 3*points[0])
        root.update()
        temp *= temp_multiplier


button = Button(root, text="Im Button", command=on_click)
button.pack()

root.mainloop()

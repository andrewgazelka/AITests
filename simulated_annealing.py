import math
import random
from tkinter import Tk, Canvas


def distance2(point_list: list):
    dist2_sum = 0
    for i in range(len(point_list) - 1):
        a = point_list[i]
        b = point_list[i + 1]
        dist2_sum += point_distance2(a, b)
    dist2_sum += point_distance2(point_list[-1], point_list[0])
    return dist2_sum


def point_distance2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


if __name__ == "__main__":
    point_num = 20
    max_x = 300
    max_y = 300

    points = [(random.random() * max_x, random.random() * max_y) for i in range(point_num)]
    # points = [(0, 300), (300, 300), (300, 0), (0, 0)]
    temp = 100_000
    temp_multiplier = .995
    temp_threshold = 200
    current = -1E10

    root = Tk()
    root.title("Title")
    root.geometry("300x300")

    c = Canvas(root, width=max_x, height=max_y)
    c.pack()
    # c.pack()

    count = 0


    def on_click():
        global temp
        global points
        global current
        if temp > temp_threshold:
            c.delete("all")
            idx = range(len(points))
            i1, i2 = random.sample(idx, 2)
            points_copied = points.copy()
            points_copied[i1], points_copied[i2] = points_copied[i2], points_copied[i1]
            result = -distance2(points_copied)
            exponent = result - current

            probability_accept = 1.0 if exponent > 0 else math.e ** (exponent / temp)

            for point in points:
                x = point[0]
                y = point[1]
                c.create_oval(x - 3, y - 3, x + 3, y + 3)
            if probability_accept > random.random():
                # print("accepted", probability_accept)
                current = result
                points = points_copied
            else:
                pass
                # print("denied:", probability_accept)
                # print("set: ", points_copied)
                # print("old: ", current, "new: ", result)

            # print("temp:", temp)

            for i in range(len(points) - 1):
                c.create_line(3 * points[i], 3 * points[i + 1])
            c.create_line(3 * points[-1], 3 * points[0])
            root.update()
            temp *= temp_multiplier

            root.after(5, on_click)
        else:
            print("done")


    # button = Button(root, text="Im Button", command=on_click)
    # button.pack()
    on_click()
    root.mainloop()

import matplotlib.pyplot as plt
from matplotlib.path import Path


def IsPointInPolygon(point):
    path = Path(cords2)
    for point in points:
        if path.contains_point(point):
            print(f"Точка {point} лежит внутри полигона")
        else:
            print(f"Точка {point} лежит снаружи полигона")


cords2 = [(-4, 0), (-3, 4), (2, 5), (6, 5), (7, 3), (8, -1), (6, -4), (4, -5), (1, -5), (-1, -4)]
points = [(-2, 2), (2, 0), (6, -2), (2, -4), (0, 6), (-2, -4), (7, -3)]

IsPointInPolygon(points)
cords2.append(cords2[0])
xs, ys = zip(*cords2)
plt.figure()
plt.plot(xs, ys)
xs, ys = zip(*points)
plt.scatter(xs, ys, color="red")
plt.grid()
plt.show()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

points = np.array([
    [0, 0],
    [2, 1],
    [1, 1],
    [-2, 2],
    [-1, 1],
    [-1, -1]
])

polygons = [
    [0, 1, 2, 0],
    [2, 3, 4, 2],
    [5, 2, 4, 5]    
]

plt.figure()
plt.plot(points[:, 0], points[:, 1], 'ko')

for polygon in polygons:
    for i in range(len(polygon) - 1):
        plt.plot(
            [points[polygon[i], 0], points[polygon[i + 1], 0]],
            [points[polygon[i], 1], points[polygon[i + 1], 1]],
            'k-'
        )

chords = [
    [4, 2],  # A5A3
    [0, 2]   # A1A3
]

for chord in chords:
    plt.plot(
        [points[chord[0], 0], points[chord[1], 0]],
        [points[chord[0], 1], points[chord[1], 1]],
        'b-'
    )

labels = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
for i, txt in enumerate(labels):
    plt.annotate(txt, (points[i, 0], points[i, 1]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.gca().set_aspect('equal', adjustable='box')
plt.show()
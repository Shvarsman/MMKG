import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mx, my, mz = 1, 2, 3

vertices = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, mx, 0, 0, color='r')
ax.quiver(0, 0, 0, 0, my, 0, color='g')
ax.quiver(0, 0, 0, 0, 0, mz, color='b')
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='r', marker='o')
ax.plot([vertices[0, 0], vertices[1, 0]], [vertices[0, 1], vertices[1, 1]], [vertices[0, 2], vertices[1, 2]], 'r-')
ax.plot([vertices[0, 0], vertices[2, 0]], [vertices[0, 1], vertices[2, 1]], [vertices[0, 2], vertices[2, 2]], 'g-')
ax.plot([vertices[0, 0], vertices[3, 0]], [vertices[0, 1], vertices[3, 1]], [vertices[0, 2], vertices[3, 2]], 'b-')
ax.plot([vertices[1, 0], vertices[2, 0]], [vertices[1, 1], vertices[2, 1]], [vertices[1, 2], vertices[2, 2]], 'r-')
ax.plot([vertices[1, 0], vertices[3, 0]], [vertices[1, 1], vertices[3, 1]], [vertices[1, 2], vertices[3, 2]], 'g-')
ax.plot([vertices[2, 0], vertices[3, 0]], [vertices[2, 1], vertices[3, 1]], [vertices[2, 2], vertices[3, 2]], 'b-')
ax.set_xlim([0, 1.5])
ax.set_ylim([0, 1.5])
ax.set_zlim([0, 1.5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Аксонометрическая проекция тетраэдра')
plt.grid(True)
plt.show()
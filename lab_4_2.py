import matplotlib.pyplot as plt

points = [(-9, 1), (-9, 2), (-4, -8), (2, -8), (9, 5)]

def is_in_circumcircle(triangle, point):
    ax, ay = triangle[0]
    bx, by = triangle[1]
    cx, cy = triangle[2]
    dx, dy = point

    a = ax - dx
    b = ay - dy
    c = (ax**2 - dx**2) + (ay**2 - dy**2)
    d = bx - dx
    e = by - dy
    f = (bx**2 - dx**2) + (by**2 - dy**2)
    g = cx - dx
    h = cy - dy
    i = (cx**2 - dx**2) + (cy**2 - dy**2)

    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    return det > 0

def delaunay(points):
    supertriangle = [(-1000, -1000), (1000, -1000), (0, 1000)]
    triangles = [supertriangle]

    for point in points:
        bad_triangles = []
        polygon = []

        for triangle in triangles:
            if is_in_circumcircle(triangle, point):
                bad_triangles.append(triangle)
                polygon.append((triangle[0], triangle[1]))
                polygon.append((triangle[1], triangle[2]))
                polygon.append((triangle[2], triangle[0]))

        triangles = [triangle for triangle in triangles if triangle not in bad_triangles]

        for edge in polygon:
            if polygon.count(edge) == 1:
                triangles.append([edge[0], edge[1], point])

    triangles = [triangle for triangle in triangles if not any(vertex in supertriangle for vertex in triangle)]
    return triangles

triangles = delaunay(points)

plt.figure()

for triangle in triangles:
    triangle.append(triangle[0])
    xs, ys = zip(*triangle)
    plt.plot(xs, ys, 'r')

plt.scatter(*zip(*points))

for i, point in enumerate(points):
    plt.text(point[0], point[1], f'A{i+1}', fontsize=12, ha='right')

plt.show()
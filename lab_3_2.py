import matplotlib.pyplot as plt

def left_clip(p, q, u1, u2):
    if p < 0:
        r = q / p
        if r > u2:
            return False, u1, u2
        elif r > u1:
            u1 = r
    elif p > 0:
        r = q / p
        if r < u1:
            return False, u1, u2
        elif r < u2:
            u2 = r
    elif q < 0:
        return False, u1, u2

    return True, u1, u2

def clip_segment(p1, p2, clip_polygon):
    x1, y1 = p1
    x2, y2 = p2
    u1, u2 = 0, 1

    for i in range(len(clip_polygon)):
        x3, y3 = clip_polygon[i]
        x4, y4 = clip_polygon[(i + 1) % len(clip_polygon)]

        dx = x4 - x3
        dy = y4 - y3

        if dx == 0 and dy == 0:
            continue

        p = -dx
        q = x1 - x3
        accept, u1, u2 = left_clip(p, q, u1, u2)

        if not accept:
            return None

        p = dx
        q = x3 + dx - x1
        accept, u1, u2 = left_clip(p, q, u1, u2)

        if not accept:
            return None

        p = -dy
        q = y1 - y3
        accept, u1, u2 = left_clip(p, q, u1, u2)

        if not accept:
            return None

        p = dy
        q = y3 + dy - y1
        accept, u1, u2 = left_clip(p, q, u1, u2)

        if not accept:
            return None

    clipped_p1 = (x1 + u1 * (x2 - x1), y1 + u1 * (y2 - y1))
    clipped_p2 = (x1 + u2 * (x2 - x1), y1 + u2 * (y2 - y1))

    return clipped_p1, clipped_p2

A = (1, 1)
B = (2, -1)
C = [(0, 0), (1, 0), (2, 1), (1, 2), (0, 1), (0, 0)]

P1 = (1, 1)
P2 = (4/3, 1/3)

clipped_segment = clip_segment(P1, P2, C)

fig, ax = plt.subplots()

ax.plot([A[0], B[0]], [A[1], B[1]], 'black', label='Исходный отрезок')
plt.scatter(*zip(A, B), color='black')
plt.scatter(*zip(P1, P2), color='b', label='Точки отсечения')

ax.plot([P1[0], P2[0]], [P1[1], P2[1]], 'black',)

if clipped_segment:
    clipped_p1, clipped_p2 = clipped_segment
    ax.plot([clipped_p1[0], clipped_p2[0]], [clipped_p1[1], clipped_p2[1]], 'black', label='Отсеченный отрезок')

x, y = zip(*C)
plt.plot(x, y, 'black')

ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Отсечение отрезка выпуклым полигоном')
ax.grid(True)

plt.show()
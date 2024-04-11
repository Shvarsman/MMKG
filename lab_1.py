import matplotlib.pyplot as plt

def sign(ch):
    if ch == 0: return 0
    if ch > 0: return 1
    if ch < 0: return -1

def CordsToVectors(cords):
    vec = []
    for i in range(len(cords) - 1):
        vec.append([cords[i+1][0] - cords[i][0], cords[i+1][1] - cords[i+1][0]])
    return vec
def IsVipucliy(cords):
    vec = CordsToVectors(cords)
    sgn = sign(vec[0][0] * vec[1][ 1] - vec[0][1] * vec[1][0])
    for i in range(1, len(vec)-1):
        cur = sign(vec[i][0] * vec[i + 1][1] - vec[i][1] * vec[i + 1][0])
        if not cur == sgn:
            if not cur == 0:
                return "Невыпуклый"
    return "Выпуклый"

def Graph(cords):
    cords.append(cords[0])
    xs, ys = zip(*cords)
    plt.figure()
    plt.plot(xs, ys)
    plt.show()

cords1 = [[-2, -3], [5, 0], [-2, 3], [2, 2], [-4, -5]]
print(IsVipucliy(cords1))
Graph(cords1)
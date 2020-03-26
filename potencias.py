import numpy as np
np.set_printoptions(suppress=True)

Amatrix = ([[6, 5, -5],
            [2, 6, -2],
            [2, 5, -1]])

Bmatrix = ([[4, -1, 1],
            [-1, 3, -2],
            [1, -2, 3]])

Cmatrix = ([[0, 1],
            [1, 1]])

ymatrix = ([1, 1])
xmatrix = ([1, 2, 3])



def normaInfinito(v):
    maxv: float
    maxv = v[0]
    for i in range(0, len(v)):
        if abs(v[i]) >= maxv:
            maxv = abs(v[i])
    return maxv


def maxNoZero(v):
    return max([x for x in v if x !=0])



def normalizarVector(v):
    w = [0]*len(v)
    for i in range(0, len(v)):
        w[i] = v[i] / normaInfinito(v)
    return w



def productoMatrizVector(m, v):
    rows = len(m)
    w = [0]*rows
    suma = 0
    for j in range(rows):
        mi = m[j]
        for i in range(len(v)):
            suma += mi[i]*v[i]
        w[j], suma = suma, 0

    return w



def metodoPotencias(A, x, M,):
    y = []
    r:  float
    r0: float
    i: int
    for i in range(0, M):
        print(i, ":")
        print("y =", y)
        print("x =", x)
        r0 = maxNoZero(x)
        y = productoMatrizVector(A, x)
        x = y
        r = maxNoZero(x)/r0
        x = normalizarVector(y)
        print("r =", r)



metodoPotencias(Amatrix, xmatrix, 200)










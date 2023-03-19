# №1
def smalldet(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]


A1 = [[4, 3],
      [1, 1]]
# print(smalldet(A1))
# print()


# №2
def submatrix(A, i, j):
    B = []
    n = len(A)
    counter = 0
    for k in range(n):
        if k == i:
            continue
        B.append([])
        for h in range(n):
            if h == j:
                continue
            B[counter].append(A[k][h])
        counter += 1
    return B


A2 = [[0, 2, 1],
      [1, 4, 3],
      [2, 1, 1]]
# print(submatrix(A2, 0, 0))
# print(submatrix(A2, 1, 1))
# print(submatrix(A2, 2, 1))
# print()


# №3
def det(A, i=0):
    n = len(A)
    result = 0
    if n == 1:
        return A
    elif n == 2:
        return smalldet(A)
    else:
        for j in range(n):
            minor = submatrix(A, i, j)
            sign = (-1) ** (i+j)
            result += sign * A[i][j] * det(minor)
        return result


A3 = [[0, 2, 1, 4],
      [1, 0, 3, 2],
      [0, 1, 4, 0],
      [1, 2, 1, 1]]

# print(det(A3))
# print()


# №4
def minor(A, i, j):
    return det(submatrix(A, i, j))


# print(minor(A3, 0, 1))
# print()


# №5
def alg(A, i=1, j=1):
    sign = (-1) ** (i+j)
    minor_ = minor(A, i, j)
    result = sign * minor_
    return result


# print(alg(A3))
# print()


# №6
def algmatrix(A):
    B = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    n = len(A)
    for i in range(n):
        for j in range(n):
            B[i][j] = alg(A, i, j)
    return B


# print(algmatrix(A3))
# print()


# №7
def transpose(A):
    n = len(A)
    B = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    for i in range(len(A[0])):
        for j in range(n):
            B[i][j] = A[j][i]
    return B


def inv(A):
    B = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    n = len(A)
    B = transpose(A)
    C = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    B = algmatrix(B)
    for i in range(n):
        for j in range(n):
            C[i][j] = B[i][j] / det(A)
    return C


# print(inv(A3))
# print()


# №8
def mult(A, B):
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def moore_penrose(H):
    return mult(inv(mult(transpose(H), H)), transpose(H))


# print(moore_penrose(A3))

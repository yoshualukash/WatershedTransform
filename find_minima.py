# Yoshua Lukas
# 1313617021
import numpy as np
import matplotlib.pyplot as plt

X = np.random.randint(1, 10, (5, 5))
print(X)


def find_minima(X):
    new_X = []
    # baris 1
    if X[0][0] <= X[0][1] and X[0][0] <= X[1][0] and X[0][0] <= X[1][1]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[0][1] <= X[0][0] and X[0][1] <= X[0][2] and X[0][1] <= X[1][0] and X[0][1] <= X[1][1] and X[0][1] <= X[1][2]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[0][2] <= X[0][1] and X[0][2] <= X[0][3] and X[0][2] <= X[1][1] and X[0][2] <= X[1][2] and X[0][2] <= X[1][3]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[0][3] <= X[0][2] and X[0][3] <= X[0][4] and X[0][3] <= X[1][2] and X[0][3] <= X[1][3] and X[0][3] <= X[1][4]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[0][4] <= X[0][3] and X[0][4] <= X[1][3] and X[0][4] <= X[1][4]:
        new_X.append(0)
    else:
        new_X.append(1)
    # baris 2
    if X[1][0] <= X[1][1] and X[1][0] <= X[0][0] and X[1][0] <= X[0][1] and X[1][0] <= X[2][0] and X[1][0] <= X[2][1]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[1][1] <= X[1][0] and X[1][1] <= X[1][2] and X[1][1] <= X[0][0] and X[1][1] <= X[0][1] and X[1][1] <= X[0][2] and X[1][1] <= X[2][0] and X[1][1] <= X[2][1] and X[1][1] <= X[2][2]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[1][2] <= X[1][1] and X[1][2] <= X[1][3] and X[1][2] <= X[0][1] and X[1][2] <= X[0][2] and X[1][2] <= X[0][3] and X[1][2] <= X[2][1] and X[1][2] <= X[2][2] and X[1][2] <= X[2][3]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[1][3] <= X[1][2] and X[1][3] <= X[1][4] and X[1][3] <= X[0][2] and X[1][3] <= X[0][3] and X[1][3] <= X[0][4] and X[1][3] <= X[2][2] and X[1][3] <= X[2][3] and X[1][3] <= X[2][4]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[1][4] <= X[1][3] and X[1][4] <= X[0][3] and X[1][4] <= X[0][4] and X[1][4] <= X[2][3] and X[1][4] <= X[2][4]:
        new_X.append(0)
    else:
        new_X.append(1)
    # baris 3
    if X[2][0] <= X[2][1] and X[2][0] <= X[1][0] and X[2][0] <= X[1][1] and X[2][0] <= X[3][0] and X[2][0] <= X[3][1]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[2][1] <= X[2][0] and X[2][1] <= X[2][2] and X[2][1] <= X[1][0] and X[2][1] <= X[1][1] and X[2][1] <= X[1][2] and X[2][1] <= X[3][0] and X[2][1] <= X[3][1] and X[2][1] <= X[3][2]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[2][2] <= X[2][1] and X[2][2] <= X[2][3] and X[2][2] <= X[1][1] and X[2][2] <= X[1][2] and X[2][2] <= X[1][3] and X[2][2] <= X[3][1] and X[2][2] <= X[3][2] and X[2][2] <= X[3][3]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[2][3] <= X[2][2] and X[2][3] <= X[2][4] and X[2][3] <= X[1][2] and X[2][3] <= X[1][3] and X[2][3] <= X[1][4] and X[2][3] <= X[3][2] and X[2][3] <= X[3][3] and X[2][3] <= X[3][4]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[2][4] <= X[2][3] and X[2][4] <= X[1][3] and X[2][4] <= X[1][4] and X[2][4] <= X[3][3] and X[2][4] <= X[3][4]:
        new_X.append(0)
    else:
        new_X.append(1)
    # baris 4
    if X[3][0] <= X[3][1] and X[3][0] <= X[2][0] and X[3][0] <= X[2][1] and X[3][0] <= X[4][0] and X[3][0] <= X[4][1]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[3][1] <= X[3][0] and X[3][1] <= X[3][2] and X[3][1] <= X[2][0] and X[3][1] <= X[2][1] and X[3][1] <= X[2][2] and X[3][1] <= X[4][0] and X[3][1] <= X[4][1] and X[3][1] <= X[4][2]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[3][2] <= X[3][1] and X[3][2] <= X[3][3] and X[3][2] <= X[2][1] and X[3][2] <= X[2][2] and X[3][2] <= X[2][3] and X[3][2] <= X[4][1] and X[3][2] <= X[4][2] and X[3][2] <= X[4][3]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[3][3] <= X[3][2] and X[3][3] <= X[3][4] and X[3][3] <= X[2][2] and X[3][3] <= X[2][3] and X[3][3] <= X[2][4] and X[3][3] <= X[4][2] and X[3][3] <= X[4][3] and X[3][3] <= X[4][4]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[3][4] <= X[3][3] and X[3][4] <= X[2][3] and X[3][4] <= X[2][4] and X[3][4] <= X[4][3] and X[3][4] <= X[4][4]:
        new_X.append(0)
    else:
        new_X.append(1)
    # baris 5
    if X[4][0] <= X[4][1] and X[4][0] <= X[3][0] and X[4][0] <= X[3][1]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[4][1] <= X[4][0] and X[4][1] <= X[4][2] and X[4][1] <= X[3][0] and X[4][1] <= X[3][1] and X[4][1] <= X[3][2]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[4][2] <= X[4][1] and X[4][2] <= X[4][3] and X[4][2] <= X[3][1] and X[4][2] <= X[3][2] and X[4][2] <= X[3][3]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[4][3] <= X[4][2] and X[4][3] <= X[4][4] and X[4][3] <= X[3][2] and X[4][3] <= X[3][3] and X[4][3] <= X[3][4]:
        new_X.append(0)
    else:
        new_X.append(1)
    if X[4][4] <= X[4][3] and X[4][4] <= X[3][3] and X[4][4] <= X[3][4]:
        new_X.append(0)
    else:
        new_X.append(1)
    return new_X


a = find_minima(X)
minima = np.reshape(a, (5, 5))
print(minima)
plt.imshow(minima, cmap='gray')
plt.show()

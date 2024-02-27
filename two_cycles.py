import random
from sympy.combinatorics import Permutation
Y = {-1: 0, 0:1, 1:1}
N = 4
Stats = {}
for k in range(2, N + 1):
    Y[k] = Y[k - 1] + (k - 1) * Y[k - 2]
for iter in range(100000):
    Q = list(range(N))
    random.shuffle(Q)
    M = N
    P = []
    while M > 0:
        if random.uniform(0.0, Y[M]) < Y[M - 1]: 
            P.append([Q[M - 1]])
            M -= 1
        else:
            P.append([Q[M - 1] , Q[M - 2]])
            M -= 2
    P = tuple(Permutation(P).array_form)
    if P in Stats:
        Stats[P] += 1
    else:
        Stats[P] = 1
print(Stats)

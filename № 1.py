L, V, T = map(int, input().split())
S = V * T
O = S / L
if O % 2 == 0:
    print(0)
else:
    D = S - (int(O) * L)
    print(D)
def f(n):
    k = 0
    for i in range(len(n)):
        k+=int(n[i])
    return k


for n in range(1,1000):
    b = bin(n)[2:]
    if f(b)%2 == 0: b = '10' + b[2:] + '0'
    else: b = '11' + b[2:] + '1'
    r = int(b,2)
    if r>=16:
        print(n)
        break

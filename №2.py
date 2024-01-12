a, b = map(int, input().split())
i = 1
k = 0

while a>= 1 and b >=1:

    if i % 2 != 0:
        k += (a + b) * 2 - 4
    else:
        k += 0
    a-=2
    b-=2
    i+=1

print(k)


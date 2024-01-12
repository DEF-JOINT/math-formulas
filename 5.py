for n in range(9999, 1001, -1):
    a = [int(c) for c in str(n)]
    s1 = a[0] + a[1]
    s2 = a[1] + a[2]
    s3 = a[2] + a[3]
    l = [s1,s2,s3]
    m = min(s1, s2, s3)
    if m == s1:
       l.remove(s1)
    elif m == s2:
        l.remove(s2)
    else:
        l.remove(s3)

    res = str(l[1]) + str(l[0]) if l[0] > l[1] else str(l[0]) + str(l[1])
    if res == '1315':
        print(n)
        break



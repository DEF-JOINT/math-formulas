from time import time

def test_time(func):
    def wrapper(*a,**b):
        st=time()
        d = func(*a, **b)
        et=time()
        ed = et - st
        print(f'time:{ed}')
        print(f'time:{st}')
        print(f'time:{et}')
        return d
    return wrapper

@test_time
def fast_nod(a,b):
    if a<b:
        a,b = b,a
    while b:
        a,b = b,a%b
    return a

res = fast_nod(2,100)
print(res)

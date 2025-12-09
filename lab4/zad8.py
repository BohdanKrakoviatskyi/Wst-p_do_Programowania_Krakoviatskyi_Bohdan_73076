
def potenga(a,n):
    if n==0:
        print("warunek stopu n=0")
        return 1
    else:
        print(f"{a} * potega({a}, {n-1})")
        return a*potenga(a,n - 1)

potenga(2,5)
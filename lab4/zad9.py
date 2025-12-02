def fib(n):
    if n==0:
        print(f"fibonacci ({n}) = 0")
        return 0
    if n==1:
        print(f"fibonacci ({n}) = 1")
        return 1
    else:
        print(f"wywołaj fibonacci ({n-1})+fibonacci({n-2})")
        return fib(n-1)+fib(n-2)
print(fib(5))

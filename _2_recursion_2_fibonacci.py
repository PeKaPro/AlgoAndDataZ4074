
import time

"""
0 1 1 2 3 5 8 13 21 34 55 89 164

fibo(n) = fibo(n-1) + fibo(n-2)

fibo(5) = fibo(4) + fibo(3)
"""

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(10)


for n in range(41):
    t0 = time.perf_counter()
    result_n = fibonacci(n)
    t1 = time.perf_counter()
    print(f"{n=} Elapsed time: {(t1 - t0):.5f}")


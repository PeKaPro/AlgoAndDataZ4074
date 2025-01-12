import datetime
import time
from functools import lru_cache


def fibonacci(n: int, cache: dict = {}) -> int:
    # print(cache)

    if n == 0:
        return 0
    if n == 1:
        return 1

    if (n - 1) in cache.keys():
        fibo_previous_value = cache[(n - 1)]
    else:
        fibo_previous_value = fibonacci(n - 1)
        cache[(n - 1)] = fibo_previous_value

    if (n - 2) in cache.keys():
        fibo_previous_previous_value = cache[(n - 2)]
    else:
        fibo_previous_previous_value = fibonacci(n - 2)
        cache[(n - 2)] = fibo_previous_previous_value

    return fibo_previous_previous_value + fibo_previous_value


fibonacci.__defaults__[0].clear()

for n in range(2000):
    t0 = time.perf_counter()
    result_n = fibonacci(n)
    t1 = time.perf_counter()
    print(f"{n=} Elapsed time: {(t1 - t0):.5f}")

"""
n=1950 Elapsed time: 0.00079 n=1950 - Elapsed time: 0.00000
n=1951 Elapsed time: 0.00077 n=1951 - Elapsed time: 0.00000
n=1952 Elapsed time: 0.00088 n=1952 - Elapsed time: 0.00000
n=1953 Elapsed time: 0.00070 n=1953 - Elapsed time: 0.00000
n=1954 Elapsed time: 0.00075 n=1954 - Elapsed time: 0.00000
n=1955 Elapsed time: 0.00109 n=1955 - Elapsed time: 0.00000
n=1956 Elapsed time: 0.00187 n=1956 - Elapsed time: 0.00000
n=1957 Elapsed time: 0.00154 n=1957 - Elapsed time: 0.00000
n=1958 Elapsed time: 0.00105 n=1958 - Elapsed time: 0.00000
n=1959 Elapsed time: 0.00106 n=1959 - Elapsed time: 0.00000
n=1960 Elapsed time: 0.00157 n=1960 - Elapsed time: 0.00000
n=1961 Elapsed time: 0.00103 n=1961 - Elapsed time: 0.00000
n=1962 Elapsed time: 0.00096 n=1962 - Elapsed time: 0.00000
n=1963 Elapsed time: 0.00072 n=1963 - Elapsed time: 0.00000
n=1964 Elapsed time: 0.00056 n=1964 - Elapsed time: 0.00000
n=1965 Elapsed time: 0.00064 n=1965 - Elapsed time: 0.00000
n=1966 Elapsed time: 0.00094 n=1966 - Elapsed time: 0.00000
n=1967 Elapsed time: 0.00058 n=1967 - Elapsed time: 0.00000
n=1968 Elapsed time: 0.00045 n=1968 - Elapsed time: 0.00000
n=1969 Elapsed time: 0.00044 n=1969 - Elapsed time: 0.00000
n=1970 Elapsed time: 0.00045 n=1970 - Elapsed time: 0.00000
n=1971 Elapsed time: 0.00044 n=1971 - Elapsed time: 0.00000
n=1972 Elapsed time: 0.00043 n=1972 - Elapsed time: 0.00000
n=1973 Elapsed time: 0.00048 n=1973 - Elapsed time: 0.00000
n=1974 Elapsed time: 0.00045 n=1974 - Elapsed time: 0.00000
n=1975 Elapsed time: 0.00045 n=1975 - Elapsed time: 0.00000
n=1976 Elapsed time: 0.00042 n=1976 - Elapsed time: 0.00000
n=1977 Elapsed time: 0.00042 n=1977 - Elapsed time: 0.00000
n=1978 Elapsed time: 0.00042 n=1978 - Elapsed time: 0.00000
n=1979 Elapsed time: 0.00051 n=1979 - Elapsed time: 0.00000
n=1980 Elapsed time: 0.00056 n=1980 - Elapsed time: 0.00000
n=1981 Elapsed time: 0.00056 n=1981 - Elapsed time: 0.00000
n=1982 Elapsed time: 0.00044 n=1982 - Elapsed time: 0.00000
n=1983 Elapsed time: 0.00046 n=1983 - Elapsed time: 0.00000
n=1984 Elapsed time: 0.00044 n=1984 - Elapsed time: 0.00000
n=1985 Elapsed time: 0.00056 n=1985 - Elapsed time: 0.00000
n=1986 Elapsed time: 0.00061 n=1986 - Elapsed time: 0.00000
n=1987 Elapsed time: 0.00062 n=1987 - Elapsed time: 0.00000
n=1988 Elapsed time: 0.00058 n=1988 - Elapsed time: 0.00000
n=1989 Elapsed time: 0.00057 n=1989 - Elapsed time: 0.00000
n=1990 Elapsed time: 0.00056 n=1990 - Elapsed time: 0.00000
n=1991 Elapsed time: 0.00045 n=1991 - Elapsed time: 0.00000
n=1992 Elapsed time: 0.00045 n=1992 - Elapsed time: 0.00000
n=1993 Elapsed time: 0.00047 n=1993 - Elapsed time: 0.00000
n=1994 Elapsed time: 0.00047 n=1994 - Elapsed time: 0.00000
n=1995 Elapsed time: 0.00049 n=1995 - Elapsed time: 0.00000
n=1996 Elapsed time: 0.00057 n=1996 - Elapsed time: 0.00000
n=1997 Elapsed time: 0.00064 n=1997 - Elapsed time: 0.00000
n=1998 Elapsed time: 0.00053 n=1998 - Elapsed time: 0.00000
n=1999 Elapsed time: 0.00048 n=1999 - Elapsed time: 0.00000
"""


@lru_cache(1000)
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(10)
fibonacci(20)

for n in range(4000):
    t0 = time.perf_counter()
    result_n = fibonacci(n)
    t1 = time.perf_counter()
    print(f"{n=} Elapsed time: {(t1 - t0):.5f}")


########################################################################

def slow_function(a):
    time.sleep(1)
    return a * 2


print(slow_function(5))
print(slow_function(5.5))
print(slow_function("Ahoj "))
print(slow_function(("a", "b", "c")))
print(slow_function(["a", "b", "c"]))


@lru_cache(1000)
def slow_function2(a: int | float | list | tuple | str):
    time.sleep(1)
    return a * 2


print(slow_function2(5))
print(slow_function2(5.5))
print(slow_function2("Ahoj "))
print(slow_function2(("a", "b", "c")))
print(slow_function2(["a", "b", "c"]))

hash("a")

my_dict = {}
my_dict[1] = [1, 2, 3, ]
my_dict[1] = (1, 2, 3,)
my_dict[3] = "1,2,3"
my_dict[4] = 1.1
print(my_dict)

my_dict[False] = 123
my_dict[1.1] = 123
my_dict["1.1"] = 123
my_dict[(1, 1)] = 123
print(my_dict)

my_dict[[1, 1]] = 123

hash([1])


# @lru_cache()
def kdo_ma_dnes_svatek():
    """Nektere funkce neni mozne cachovat - protoze zavisi """
    dnes = datetime.datetime.today()


class FibonacciCalculator:

    def __init__(self):
        self.cache = {}

    def calculate(self, n: int):
        if n == 0:
            return 0
        if n == 1:
            return 1

        if (n-1) in self.cache.keys():
            previous_value = self.cache[(n-1)]
        else:
            previous_value = self.calculate(n-1)
            self.cache[(n - 1)] = previous_value

        if (n - 2) in self.cache.keys():
            previous_previous_value = self.cache[(n - 2)]
        else:
            previous_previous_value = self.calculate(n - 2)
            self.cache[(n - 2)] = previous_previous_value

        return previous_value + previous_previous_value

    def invalidate_cache(self):
        self.cache.clear()
        print("cache reset")




fibo = FibonacciCalculator()

fibo.calculate(100)

fibo.cache
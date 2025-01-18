
"""
0 1 1 2 3 5 8 13 21 34 55 89 144
"""

def fibonacci_iter(n: int) -> int:

    fibo_list = [0, 1]

    while len(fibo_list) < n:
        next_element = fibo_list[-1] + fibo_list[-2]
        fibo_list.append(next_element)

    return fibo_list[n-1]


print(fibonacci_iter(5))

print(fibonacci_iter(6))
print(fibonacci_iter(7))
print(fibonacci_iter(10))

#####################################

def faktorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError

    if n == 0:
        return 1
    if n == 1:
        return 1

    factorial = 1
    for element in range(n, 0, -1):
        # factorial = factorial * element
        factorial *= element

    return factorial



range(5)
list(range(5))

list(range(5, 0, -1))

n=5
list(range(1, n+1))

faktorial_iter(5)

##############################################################
"""
5 * 3 = 5 + 5 + 5
      = 3 + 3 + 3 + 3 + 3

5 * 3 = (5 * 2) + (5 * 1)
5 * 3 = (5 * 2) + (5)
"""


def nasobeni(a, b):
    if b == 0:
        return 0
    if b == 1:
        return a

    return a + nasobeni(5, b-1)



print(nasobeni(5, 3))
print(nasobeni(5, 1))
print(nasobeni(5, 0))
print(nasobeni(5, 50))
print(nasobeni(5, 5))

print(nasobeni(5, -5))






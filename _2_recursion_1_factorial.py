
"""
faktorial - funkce pro nezaporny cely cisla
5! = 5 * 4 * 3 * 2 * 1 = 120

5.37! - tohle neni definovano
-5! - tohle neni definovano

5! = 5 * 4 * 3 * 2 * 1
4! =     4 * 3 * 2 * 1

5! = 5 * 4!
4! = 4 * 3!


n! = n * (n-1)!

5! = 5 * 4 * 3!
5! = 5 * 4 * 3 * 2!
5! = 5 * 4 * 3 * 2 * 1!
5! = 5 * 4 * 3 * 2 * 1

1! = 1
0! = 1

130! = 130 * 129 * ... * 1

"""

"""
faktorial N 
if n > 1:
    n * (n-1)!
if n == 1:
    return 1

"""


def factorial_bad(n: int) -> int:
    return n * factorial_bad(n-1)


factorial_bad(5)  # 120


def factorial_not_so_good(n: int) -> int:

    # 1! = 1
    # 0! = 1
    if n in (1, 0):
        return 1

    return n * factorial_not_so_good(n - 1)


factorial_not_so_good(5)  # 120
factorial_not_so_good(0)
factorial_not_so_good(1)
factorial_not_so_good(3)
factorial_not_so_good(4)

factorial_not_so_good(-5)

factorial_not_so_good("asdf")

factorial_not_so_good(1.1)


def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError(f"Factorial only works with integers, got {type(n)}")
    if n < 0:
        raise ValueError("Factorial is defined only for non negative integers")

    # 1! = 1
    # 0! = 1
    if n in (1, 0):
        return 1

    return n * factorial(n - 1)


factorial(5)  # 120
factorial(0)
factorial(1)
factorial(3)
factorial(4)

factorial(-5)

factorial("asdf")

factorial(1.1)




class MyInt(int):
    pass


x = MyInt("3")
x + 54

type(x) == int

isinstance("3.7", (int, float))


type(x)
isinstance(x, int)


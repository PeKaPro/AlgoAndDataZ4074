import random
import statistics


def average1(values: list[int | float]) -> float:
    return sum(values) / len(values)


def average2(values: list[int | float]) -> float:
    suma = 0
    pocet = 0
    for value in values:
        suma += value
        pocet += 1
    return suma / pocet


def average3(values: list[int | float]) -> float:
    return statistics.mean(values)


for i in range(1_000):
    numbers = [random.randint(0, 1_000) for j in range(1_000)]

    zvolena_funkce = random.choice([average1, average2, average3])

    result = zvolena_funkce(numbers)

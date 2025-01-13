
import time
import random


def linear_search(li: list, value):
    for ix, list_value in enumerate(li):
        if list_value == value:
            return ix
    return None


def binary_search_iter(li: list, number: int) -> int | None:

    left = 0
    right = len(li) - 1

    while (left <= right):

        middle_ix = (left + right) // 2
        middle = li[middle_ix]

        if middle == number:
            return middle_ix
        elif middle > number:
            right = middle_ix - 1
        elif middle < number:
            left = middle_ix + 1

    return None



N = 10000
NUMBER_OF_SEARCHES = 10000

numbers = [random.randint(0, 1_000_000) for i in range(N)]
numbers.sort()

evaluated_functions = [linear_search, binary_search_iter, ]


for fn in evaluated_functions:
    start_time = time.perf_counter()
    for i in range(NUMBER_OF_SEARCHES):
        random_selected_number = random.choice(numbers)
        result = fn(numbers, random_selected_number)
    end_time = time.perf_counter()

    print(f"Elapsed time: {fn.__name__:<20} {(end_time - start_time):.10f}")


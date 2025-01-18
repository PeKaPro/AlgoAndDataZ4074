
from typing import Optional
import random


# my_list = [1, 2, 3, 4, 5, 6, 7, 85, 87, 97]
#
# 0..9
# 4
# 0..4
# 2


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


if __name__ == '__main__':

    my_list = [random.randint(0, 100_000_000) for i in range(1000)]

    print(my_list[:10])

    my_list.sort()

    print(my_list[:10])

    print(binary_search_iter(my_list, 817453))

    my_list[7]

    print(binary_search_iter(my_list, random.choice(my_list)))



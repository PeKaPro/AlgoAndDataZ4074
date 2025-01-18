import random

[10, 29, 23, 31, 6]  # start
[6, 10, 23, 29, 31]

# 1. kolo start
[[10, 29], 23, 31, 6]

[10, [29, 23], 31, 6]
[10, [23, 29], 31, 6]

[10, 23, [29, 31], 6]

[10, 23, 29, [31, 6]]
[10, 23, 29, [6, 31]]

[10, 23, 29, 6, 31]


def bubble_sort(array: list):
    pocet_kroku = 0

    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - 1 -i):
            pocet_kroku += 1

            cislo1 = array[j]
            cislo2 = array[j + 1]

            if cislo1 > cislo2:
                array[j] = cislo2
                array[j + 1] = cislo1
                already_sorted = False

        if already_sorted:
            print("pocet_kroku:", pocet_kroku)
            return array

    print("pocet_kroku:", pocet_kroku)
    return array


def bubble_sort_suboptimal(array: list):
    pocet_kroku = 0

    n = len(array)

    for i in range(n):

        for j in range(n-1):
            pocet_kroku += 1

            cislo1 = array[j]
            cislo2 = array[j+1]

            if cislo1 > cislo2:
                array[j] = cislo2
                array[j + 1] = cislo1
    print("pocet_kroku:", pocet_kroku)
    return array


if __name__ == '__main__':
    [10, 29, 23, 31, 6]
    [6, 10, 23, 29, 31]

    bubble_sort([10, 29, 23, 31, 6])

    random.seed(575)
    my_list = [random.randint(1, 999) for i in range(100)]
    print(my_list)

    # assert 1 == 0
    assert bubble_sort(my_list) == sorted(my_list)

    bubble_sort_suboptimal([10, 29, 23, 31, 6])
    bubble_sort_suboptimal([6, 10, 23, 29, 31])
    bubble_sort_suboptimal([])

    bubble_sort([10, 29, 23, 31, 6])
    bubble_sort([6, 10, 23, 29, 31])


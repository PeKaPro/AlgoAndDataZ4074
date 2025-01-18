import random

[10, 29, 23, 31, 6]

[[10, 29], 23, 31, 6]

[10, [29, 23], 31, 6]
[[10, 23], 29, 31, 6]

[10, 23, [29, 31], 6]
[10, 23, 29, [31, 6]]
[10, 23, 29, [6, 31]]
[10, 23, [29, 6], 31]
[10, 23, [6, 29], 31]

[10, [23, 6], 29, 31]
[10, [6, 23], 29, 31]

[[10, 6], 23, 29, 31]
[[6, 10], 23, 29, 31]


def insert_sort(array: list):
    n = len(array)

    for i in range(1, n):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j+1] = array[j]

            j -= 1

        array[j + 1] = item

    return array


if __name__ == '__main__':
    insert_sort([10, 29, 23, 31, 6])
    insert_sort([6, 10, 23, 29, 31])

    random.seed(575)
    my_list = [random.randint(1, 999) for i in range(100)]
    print(my_list)

    assert sorted(my_list) == insert_sort(my_list)

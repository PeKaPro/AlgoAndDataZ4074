




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


def binary_search_rec(li: list, number: int, left=None, right=None) -> int | None:
    if left is None:
        left = 0
    if right is None:
        right = len(li) - 1

    if (left <= right):
        middle_ix = (left + right) // 2
        middle = li[middle_ix]

        if middle == number:
            return middle_ix
        elif middle > number:
            right = middle_ix - 1
            return binary_search_rec(li, number, left, right)

        elif middle < number:
            left = middle_ix + 1
            return binary_search_rec(li, number, left, right)

    else:
        return None




binary_search_rec([1, 2, 3, 4],4)




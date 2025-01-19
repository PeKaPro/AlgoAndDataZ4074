import random

left = [1,3,5,7]
right = [500,1000,2000,3000]

[1,3,5,7] + [500,1000,2000,3000]

def merge(left: list, right: list) -> list:
    if len(right) == 0:
        return left
    if len(left) == 0:
        return right

    output = []
    ix_left, ix_right = 0, 0

    while len(output) < len(left) + len(right):
        if left[ix_left] < right[ix_right]:
            output.append(left[ix_left])
            ix_left += 1
        else:
            output.append(right[ix_right])
            ix_right += 1

        if ix_left == len(left):
            return output + right[ix_right:]

        if ix_right == len(right):
            return output + left[ix_left:]

    return output


def merge_sort(array: list):

    if len(array) < 2:
        return array

    ix_middle = len(array) // 2

    return merge(
        left=merge_sort(array[:ix_middle]),
        right=merge_sort(array[ix_middle:]),
    )




if __name__ == '__main__':
    merge([],[])
    merge([1,2,3,4,5,6], [])
    merge([], [1, 2, 3, 4, 5, 6] )
    merge([1,2,3,4], [10,20, 30, 40])
    merge([1, 3, 5,7], [2,4,6,8])

    print(merge_sort([10, 29, 23, 31, 6]))
    print(merge_sort([6, 10, 23, 29, 31]))

    random.seed(575)
    my_list = [random.randint(1, 999) for i in range(100)]
    print(my_list)

    assert sorted(my_list) == merge_sort(my_list)
    if sorted(my_list) == merge_sort(my_list):
        print("Funguje to")
    else:
        print("Nefunguje to")

    print(my_list)
    print(merge_sort(my_list))


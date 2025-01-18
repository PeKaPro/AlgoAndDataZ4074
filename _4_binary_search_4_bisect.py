
import bisect

my_list = [1, 2, 2, 2, 4, 7, 9]

# print(my_list)
# my_list.insert(0, -1)
# print(my_list)

bisect.bisect_left(my_list, 5)


my_list = [1, 2, 2, 2, 4, 7, 9]
index = bisect.bisect_left(my_list, 2)
bisect.bisect_right(my_list, 2)
my_list.insert(index, 2)

bisect.bisect is bisect.bisect_right

print(my_list)
bisect.insort_left(my_list, 5)
print(my_list)

print(my_list)
bisect.insort_left(my_list, 2)
print(my_list)


my_list = [1, 2, 2, 2, 4, 7, 9]
bisect.bisect_left(my_list, 4)

def binary_search_bisect_bad(li: list, number: int):
    ix = bisect.bisect_left(li, number)

    if li[ix] == number:
        return ix
    else:
        return None


def binary_search_bisect(li: list, number: int):
    ix = bisect.bisect_left(li, number)

    if ix != len(li) and li[ix] == number:
        return ix
    else:
        return None


if __name__ == '__main__':
    print(my_list)

    print(binary_search_bisect_bad(my_list, 33))


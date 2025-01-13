

my_list = [1, 87, 97, 1, 3, 5, 7, 5, 6, 7, 85, 2, 1, 4, ]

# my_list.index(85)
# my_list[10]


def linear_search(li: list, value):
    for ix, list_value in enumerate(li):
        if list_value == value:
            return ix
    return None


print(linear_search(my_list, 85))


import random

"""
[8, 2, 6, 4, 5]
[8,2], [6,4,5]
[8],[2],[6,4],[5]
[8],[2],[6],[4],[5]
[2]+[4]+[5]+[6]+[8]
"""
"""

[2, 6, 4]

pivot = 4

small = [2]
same = [4]
large = [6]

small + same + large

"""
[8, 8, 8, 8, 2, 6, 4, 5]

pivot = 8
small = [2, 6, 4, 5]
same = [8, 8, 8, 8]
large = []

# rec(small) + same + large
[2,4,5,6] + same + large

# ------
# rec(small)

[2, 6, 4, 5]

pivot = 5

small = [2, 4,]
same = [5]
large = [6]

# rec(small) + same + large
[2, 4,] + [5] + [6]
[2,4,5,6]
# -----
# rec(small)
[2, 4,]

pivot = 2
small = []
same = [2]
large = [4]

small + same + large
[2,4]


def quicksort(array: list):
    """
    chci rozdelit list na 3 sub listy,
    small - mensi hodnoty,
    same - stejne hodnoty,
    large - vetsi hodnoty

    a na ne dal aplikovat stejny postup rozdelovani
    ... az se stane ze list je prazdny nebo jednoclenny - potom vim, ze je serazeny a muzu zacit vracet vysledek
    vysledek = small + same + large
    """

    if len(array) < 2:  # ukoncovaci podminka rekurze
        return array

    small, same, large = [], [], []

    pivot = random.choice(array)  # pivot muze byt nahodne zvoleny (je to rychlejsi nez pocitat treba median)

    # distribuce hodnot do listu small, same, large...
    for element in array:
        if element < pivot:
            small.append(element)
        elif element > pivot:
            large.append(element)
        else:
            same.append(element)

    # return a rekurzivni volani
    return quicksort(small) + same + quicksort(large)


if __name__ == '__main__':
    print(quicksort([10, 29, 23, 31, 6]))
    print(quicksort([6, 10, 23, 29, 31]))

    random.seed(575)
    my_list = [random.randint(1, 999) for i in range(100)]
    print(my_list)

    assert sorted(my_list) == quicksort(my_list)

    print(my_list)
    print(quicksort(my_list))


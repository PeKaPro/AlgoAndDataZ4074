import random

# nejmensi -> nejvetsi

# odkrokovana ukazka, insert sort se snazi tlacit male elementy vic a vic doleva
[10, 29, 23, 31, 6]  # start
[6, 10, 23, 29, 31]  #ocekavany vysledek


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

    for i in range(1, n):   # zaciname od druheho elementu, protoze budeme srovnavat s elementem nalevo,
                            # element na indexu 0 zadny element nalevo nema a proto zde nemuzeme zacit.
                            # (respektive muzeme, ale nebylo by to optimalni, plytvali bychom vypocetni kapacitou)

        item = array[i]  # poznamenam si aktualni hodnotu
        j = i - 1  # j - chci se divat doleva, odectu od indexu i jednicku

        while j >= 0 and array[j] > item:  # dokud je j "nezaporne" (je to validni index) a dokud je element na pozici j vetsi nez vychozi element na pozici i
            array[j+1] = array[j]  # posouvam "vetsi element zleva" (neboli array[j]) do prava (relativne, vuci aktualni hodnote j)

            j -= 1  # jdeme vice doleva - odecitame 1 od indexu j

        array[j + 1] = item  # po skonceni while loopy musime ulozit hodnotu v promene item zpet do listu ...

    return array


if __name__ == '__main__':
    insert_sort([10, 29, 23, 31, 6])
    insert_sort([6, 10, 23, 29, 31])

    random.seed(575)
    my_list = [random.randint(1, 999) for i in range(100)]
    print(my_list)

    assert sorted(my_list) == insert_sort(my_list)

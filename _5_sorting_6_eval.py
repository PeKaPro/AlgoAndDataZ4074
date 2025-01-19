
import time
import random

from _5_sorting_2_bubble import bubble_sort
from _5_sorting_3_insertion import insert_sort
from _5_sorting_4_quicksort import quicksort
from _5_sorting_5_merge import merge_sort


random.seed(777)

SAMPLE_SIZE = 100
SAMPLE_SIZE_BIG = 100*100
REPETITION = 3


my_functions = [
    merge_sort,
    quicksort,
    insert_sort,
    bubble_sort,
]
print(my_functions)


for evaluated_function in my_functions:

    for sample_size in [SAMPLE_SIZE, SAMPLE_SIZE_BIG]:
        start_time = time.perf_counter()
        for _ in range(REPETITION):
            my_list = [random.randint(0, 999_999_999) for i in range(sample_size)]
            my_list = evaluated_function(my_list)
        elapsed_time = time.perf_counter() - start_time

        print(f"Funkce {evaluated_function.__name__} trvala {elapsed_time}s, velikost dat: {sample_size}")


"""
Funkce merge_sort trvala 0.0015724000404588878s, velikost dat: 100
Funkce merge_sort trvala 0.3346241000108421s, velikost dat: 10000 - 100x
212
 n * log n

Funkce quicksort trvala 0.001324000011663884s, velikost dat: 100
Funkce quicksort trvala 0.16297929995926097s, velikost dat: 10000
123.09614692105876

Funkce insert_sort trvala 0.002923299965914339s, velikost dat: 100
Funkce insert_sort trvala 11.628736000042409s, velikost dat: 10000
3977.9482556129733 

Funkce bubble_sort trvala 0.0029338999884203076s, velikost dat: 100
Funkce bubble_sort trvala 34.492273700016085s, velikost dat: 10000
11756.458582825679
100^2 = 10_000 

"""

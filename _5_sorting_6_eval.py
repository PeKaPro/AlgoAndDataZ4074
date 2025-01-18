
from _5_sorting_2_bubble import bubble_sort
from _5_sorting_3_insertion import insert_sort
from _5_sorting_4_quicksort import quicksort
# from _5_sorting_5_merge import merge_sort

import time
import random


random.seed(777)

SAMPLE_SIZE = 100
SAMPLE_SIZE_BIG = 100*100
REPETITION = 3


my_functions = [
    # merge_sort,
    quicksort,
    insert_sort,
    bubble_sort,
]
print(my_functions)


for evaluated_function in my_functions:

    for sample_size in [SAMPLE_SIZE, SAMPLE_SIZE_BIG]:
        start_time = time.time()
        for _ in range(REPETITION):
            my_list = [random.randint(0, 999_999_999) for i in range(sample_size)]
            my_list = evaluated_function(my_list)
        elapsed_time = time.time() - start_time

        print(f"Funkce {evaluated_function.__name__} trvala {elapsed_time}s, velikost dat: {sample_size}")


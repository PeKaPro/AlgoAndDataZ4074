
import time
import random


from _4_binary_search_1_linear import linear_search
from _4_binary_search_2_iter import binary_search_iter
from _4_binary_search_3_rec import binary_search_rec
from _4_binary_search_4_bisect import binary_search_bisect




N1 = 1_000
N2 = 1_000_000
NUMBER_OF_SEARCHES = 1_000

numbers_1 = [random.randint(0, 1_000_000_000) for i in range(N1)]
numbers_1.sort()

numbers_2 = [random.randint(0, 1_000_000_000) for i in range(N2)]
numbers_2.sort()

evaluated_functions = [binary_search_iter, binary_search_rec, binary_search_bisect, linear_search]

for fn in evaluated_functions:
    start_time = time.perf_counter()
    for i in range(NUMBER_OF_SEARCHES):
        random_selected_number = random.choice(numbers_2)
        result = fn(numbers_2, random_selected_number)
    end_time = time.perf_counter()

    print(f"Elapsed time: {fn.__name__:<20} {(end_time - start_time):.10f}")



"""
numbers_1 = 1 000 elementu
Elapsed time: binary_search_iter   0.0020969000
Elapsed time: binary_search_rec    0.0044237000
Elapsed time: binary_search_bisect 0.0014952000
Elapsed time: linear_search        0.0295844000
                                   029.5844000


numbers_2 = 1 000 000 elementu
Elapsed time: binary_search_iter   0.0101450000
Elapsed time: binary_search_rec    0.0101799000
Elapsed time: binary_search_bisect 0.0069528000
Elapsed time: linear_search        67.2250437000

"""
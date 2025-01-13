
from dataclasses import dataclass
from memory_profiler import profile

N = 10_000_000


class Record:
    def __init__(self, a: int):
        self.a = a


@dataclass(slots=True, frozen=True)
class RecordSimple:
    a: int




def generate_numbers_range():
    return range(N)


def generate_numbers_list():
    return list(range(N))


def generate_numbers_tuple():
    return tuple(range(N))


def generate_numbers_set():
    return set(range(N))


def generate_numbers_class():
    return [Record(i) for i in range(N)]


def generate_numbers_class2():
    """alternativni zapis generate_numbers_class"""
    data = []
    for i in range(10_000_000):
        record = Record(i)
        data.append(record)
    return data


def generate_numbers_dataclass():
    return [RecordSimple(i) for i in range(N)]





@profile
def main():
    a = generate_numbers_range()
    b = generate_numbers_list()
    c = generate_numbers_tuple()
    d = generate_numbers_set()
    # e = generate_numbers_class()
    f = generate_numbers_dataclass()


    del a
    del b
    del c
    del d
    # del e
    del f


if __name__ == '__main__':
    main()




# mutable - menitelny # list, dict, set
# immutable - nezmenitelny... # tuple, frozenset


default_list = []

def my_function(a: int, b: list = default_list) -> None:
    print(b)
    b.append(a)
    print(b)


my_function(50, [])
my_function(3)

default_list

print(my_function)
"asdf".upper()
my_function.__defaults__[0].append("Ahoj")



def fn(a: int, b:int=123):
    pass

fn.__defaults__
fn.__annotations__

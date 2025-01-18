
import random

random.seed(575)  # toto zpusobi, ze hodnoty vygenerovane "nahodne" budou pokazde stejne sekvence nahodnych cisel
my_list = [random.randint(1, 999) for i in range(100)]
print(my_list)


# metoda list.sort seradi list, na kterem je pouzita
print(my_list)
my_list.sort()
print(my_list)



random.seed(575)
my_list = [random.randint(1, 999) for i in range(100)]
print(my_list)

# funkce sorted vytvori novy, serazeny list, puvodni list zustane neserazeny
print(my_list)
my_new_list = sorted(my_list)
print(my_list)
print(my_new_list)


# timsort - algoritmus, ktery je v pythonu pouzit pro sorting
# kompozitni algoritmus
# vyuziva toho, ze v datech realneho sveta casto byvaji "ostruvky" - sekvence cisel - ktere jsou uz serazene



# jak se porovnavaji ruzne datove typy - stringy se prevedou na ciselne hodnoty
my_letters = ["a", "c", "b"]
sorted(my_letters)

if "a" < "b":
    print(123)

if 97 < 98:
    print(123)

my_dict = {
    "a": 5,
    "b": 1,
    "c": 20
}

# jak z dictu najit klic s nejmensi hodnotou
min(my_dict)
min(my_dict, key=my_dict.get)

my_list = [
    (15, 20, 1),
    (15, 5, 100),
    (10, 5, 5)
]
sorted(my_list, reverse=False)  # default


# porovnavani vlastnich objektu - musi se definovat metoda jako __gt__ (vetsi nez, >)
class MyClass:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        return self.a > other.a

    def __ge__(self, other):
        return self.a >= other.a


x = MyClass(5)
y = MyClass(50)

x > y
x >= y

my_list = [
    MyClass(5),
    MyClass(10),
    MyClass(-5)
]

print(my_list)

my_sorted_list = sorted(my_list)

for x in my_sorted_list:
    print(x.a)


class MojeTrida:

    def __init__(self, a):
        self.a = a

    def funkce(self):
        print(123)

moje_instance = MojeTrida(5)

moje_instance.a
moje_instance.funkce()

moje_instance.a = 15
print(moje_instance.a)

moje_instance.neco_noveho = 15
print(moje_instance.neco_noveho)

moje_instance.b = 15
print(moje_instance.b)

moje_instance.c = 15
print(moje_instance.c)

moje_instance.funkce = "Haha, uz tu zadna funckce neni."

moje_instance.funkce



def moje_funkce():
    print("Hmm, nova funkce, kterou mozna natlacim do klassy")

moje_instance.nova_funkce = moje_funkce

moje_instance.nova_funkce()


moje_instance.__class__.__name__

moje_instance.__dict__
moje_instance.xxxxxxx = 159
moje_instance.__dict__

moje_instance.__slots__


class MojeTrida2:

    def __init__(self, a):
        self.a = a

    def fn(self):
        print("fn")

    __slots__ = ("a",)



moje_instance2 = MojeTrida2(55)
moje_instance2.a
moje_instance2.a = 33
moje_instance2.a

moje_instance2.asdf = 147
moje_instance2.__slots__

moje_instance2.fn()

moje_instance2.print = print

@classmethod
def fn():
    pass


moje_instance2.fn2 = fn


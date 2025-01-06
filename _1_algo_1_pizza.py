

# Prirozeny jazyk
"""
1. Rozvalet testo.
2. Pridat rajcatovy zaklad.
3. Pridat syr.
4. Pridat sunku.
5. Kdyz chceme cerstvy rajcata, tak je tam pridame.
6. Upect.

Jako prvni vezmeme testo a rozvalime ho...
"""

# Pseudokod
"""
1. rozvalet_testo()
2. add(rajcatovy zaklad)
3. add(syr)
4. add(ham)

5. IF (chceme rajcata) {
    add(rajcata)
}
5. if chceme rajcata:
    add(rajcata)

6. upect()
"""



class Pizza:

    def __init__(self):
        print("Valime testo...")
        self.ingredients = []
        # self.status = "raw"
        self.is_baked = False

    def add_ingredient(self, ingredient: str):
        self.ingredients.append(ingredient)

    def bake(self) -> None:
        if self.is_baked:
            print("Uz je to upeceno...")
            return
        else:
            print("Baking...")
            self.is_baked = True

    def __repr__(self) -> str:
        ingredients = ", ".join(self.ingredients)
        if self.is_baked:
            return f"Baked Pizza({ingredients})"
        else:
            return f"S(y/u)rova Pizza({ingredients})"

    # def __str__(self) -> str:
    #     pass



pizza = Pizza()
print(pizza)
pizza.add_ingredient("Maslo")
pizza.add_ingredient("Rajcata")
pizza.add_ingredient("Vajicka")
print(pizza)
pizza.bake()
print(pizza)


def make_my_pizza(chceme_rajcata: bool) -> Pizza:
    pizza = Pizza()
    pizza.add_ingredient("rajcatovy zaklad")
    pizza.add_ingredient("syr")
    pizza.add_ingredient("sunka")

    # if "rajcata" not in pizza.ingredients:
    #     pizza.add_ingredient("rajcata")

    if chceme_rajcata:
        pizza.add_ingredient("rajcata")
    else:
        print("Preskakujeme rajcata, protoze je nechceme...")

    pizza.bake()
    return pizza


def make_any_pizza(ingredients: list[str]) -> Pizza:
    pizza = Pizza()

    for ingredient in ingredients:
        pizza.add_ingredient(ingredient)

    pizza.bake()
    return pizza


def make_my_pizza2(chceme_rajcata: bool) -> Pizza:

    ingredients = ["rajcatovy zaklad", "syr", "sunka"]

    if chceme_rajcata:
        ingredients.append("rajcata")
    else:
        print("Preskakujeme rajcata, protoze je nechceme...")

    pizza = make_any_pizza(["rajcatovy zaklad", "syr", "sunka"])
    return pizza


def make_my_pizza3(chceme_rajcata: bool) -> Pizza:
    ingredients = ["rajcatovy zaklad", "syr", "sunka"]

    if chceme_rajcata:
        ingredients.append("rajcata")

    pizza = make_any_pizza(ingredients)
    return pizza




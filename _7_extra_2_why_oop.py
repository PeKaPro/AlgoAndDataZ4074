
zustatek = 5000
mena = 'czk'

def kolik_mam():
    print(zustatek, mena)

def prevest_na_eura():
    print(zustatek / 25, 'eur')


class BankovniUcet:

    def __init__(self, balance, currency:str):
        self.balance = balance
        self.currency = currency
        # self.disponents = []

    def kolik_mam(self):
        print(self.balance, self.currency)

    def prevest_na_menu(self, mena: str):
        if mena == 'eur' and self.currency == 'czk':
            print(self.balance / 25)
            return
        raise NotImplementedError(f"neznamy kurz {mena}")


bu1 = BankovniUcet(5000, 'czk')
bu1.kolik_mam()
bu1.prevest_na_menu('eur')


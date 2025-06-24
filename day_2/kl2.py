class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner # self - obiekt klasy
        self._balance = balance

    @property  # getter
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Saldo nie może być ujemne")
        self._balance = value

    @property
    def is_rich(self):
        return self._balance > 1_000_000


konto = BankAccount("Jan Kowalski", 50000)
print(f'Aktualne saldo: {konto.balance} zł')  # Aktualne saldo: 50000 zł
konto.balance += 12000
print(f'Nowe saldo: {konto.balance} zł')  # Nowe saldo: 62000 zł

print(f"CZy własciciel ma status VIP? {konto.is_rich}")  # CZy własciciel ma status VIP? False

try:
    konto.balance = -9000
except ValueError as ve:
    print("Bład:", ve)  # Bład: Saldo nie może być ujemne

konto._balance = 10
print(konto.balance)  # 10

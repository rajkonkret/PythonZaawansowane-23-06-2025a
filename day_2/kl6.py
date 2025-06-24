from functools import singledispatchmethod


# przeciążanie

class Printer:

    @singledispatchmethod
    def print(self, val):
        print("Nieznany typ")

    @print.register
    def _(self, val: int):
        print(f"Int: {val}")

    @print.register
    def _(self, val: str):
        print(f'Str: {val}')


p = Printer()
p.print(123)
p.print("Tekst")
# Int: 123
# Str: Tekst

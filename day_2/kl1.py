# PascalCase - UpperCamelCase
class Person:
    def __init__(self, name, age):
        self.__name = name  # pole prywatne
        self.__age = age

    def nowe_imie(self, str):
        self.__name = str

    def nowy_wiek(self, wiek):
        self.__age = wiek

    def __str__(self):
        return f"{self.__name}, wiek: {self.__age}"

    def __repr__(self):
        return f"{self.__name}, (wiek: {self.__age})"


ob = Person("Radek", 50)
print(ob)  # <__main__.Person object at 0x00000284F27E6E40>
# po dodaniu __str__
# Radek, wiek: 50
ob2 = Person("Nana", 89)
print(ob)  # Radek, wiek: 50

lista = [ob, ob2]
print(lista)
# [<__main__.Person object at 0x0000023041696E40>, <__main__.Person object at 0x0000023041928CD0>]
# po nadpisaniu __repr__
# [Radek, (wiek: 50), Nana, (wiek: 89)]

# pole prywatne, nie jest widoczne poza klasą
# print(ob.__name) # AttributeError: 'Person' object has no attribute '__name'
ob.__name = "Tomek"
print(ob)
# Radek
# Tomek, wiek: 50

ob.nowy_wiek(67)
print(ob)  # Tomek, wiek: 67

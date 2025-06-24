from desc1 import Person
from desc2 import MClass
from desc3 import MojLog

print("Przykład desc1")
try:
    p = Person("Jan", 56)
    print(p.name)
    print(p.age)

    p.age = "szesnascie"
    print(p.age)  # Bład: Oczekiwano wartości typu: <class 'int'>
except TypeError as e:
    print("Bład:", e)

print("Przykład desc2")
try:
    ob = MClass()
    print(ob.constant)
    ob.constant = 900
except AttributeError as e:
    print("Bład:", e)  # Bład: To jest tylko do ODCZYTU!

print("Przykłąd desc3")

try:
    print("_" * 50)
    trzeci = MojLog()
    trzeci.x = 10
    print(trzeci.x)

    print("_" * 50)
    del trzeci.x
    print(trzeci.x)

    print("_" * 50)
    del trzeci.y
    print(trzeci.y)
except Exception as e:
    print("Bład:", e)
# __________________________________________________
# Ustawienie wartości: 10
# 10
# __________________________________________________
# Usuwanie atrybutu. Poprzednia wartość: 10
# 0
# __________________________________________________
# Usuwanie atrybutu. Poprzednia wartość: brak
# brak

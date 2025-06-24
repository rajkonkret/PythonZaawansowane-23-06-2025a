from desc1 import Person
from desc2 import MClass

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

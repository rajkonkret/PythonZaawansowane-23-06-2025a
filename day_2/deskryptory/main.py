from desc1 import Person

print("Przykład desc1")
try:
    p = Person("Jan", 56)
    print(p.name)
    print(p.age)

    p.age = "szesnascie"
    print(p.age)  # Bład: Oczekiwano wartości typu: <class 'int'>
except TypeError as e:
    print("Bład:", e)

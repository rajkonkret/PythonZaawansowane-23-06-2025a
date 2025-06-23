# funkcja - pozwakla wykonac kod dowolną ilośc razy
# dzieki funnkcji unikamy dublowania kodu
def factorial(n):
    if n == 0 or n == 1:
        return 1
    # funkcja rekurencyjna, wywołuje samą siebie
    return n * factorial(n - 1)


print(f"Silnia z 7 wynosi: {factorial(7)}")  # Silnia z 7 wynosi: 5040


# funkcja filtruje parzyste
def filter_even(numbers):
    lista_wynik = []
    for num in numbers:
        if num % 2 == 0:  # modulo - reszta z dzielenia
            lista_wynik.append(num)
    return lista_wynik


def filter_even_lc(numbers):
    return [num for num in numbers if num % 2 == 0]
    # list comprehensions - lista anonimowa


liczby = [5, 2, 8, 3, 23, 78, 9, 32, 6, 8, 0, -23, 57, 43, 68, 44, 66, 11, 12]
print(filter_even(liczby))  # [2, 8, 78, 32, 6, 8, 0, 68, 44, 66, 12]
print(filter_even_lc(liczby))  # [2, 8, 78, 32, 6, 8, 0, 68, 44, 66, 12]


def word_count(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


print(word_count("Hello world hello Python Python world Hello everybody"))
# {'hello': 3, 'world': 2, 'python': 2, 'everybody': 1}

from collections import Counter


def word_counter_collections(text):
    words = text.lower().split()
    return Counter(words)


print(word_counter_collections("Hello world hello Python Python world Hello everybody"))


# Counter({'hello': 3, 'world': 2, 'python': 2, 'everybody': 1})

def word_counter_collections_dict(text):
    words = text.lower().split()
    return dict(Counter(words))


print(word_counter_collections_dict("Hello world hello Python Python world Hello everybody"))


# {'hello': 3, 'world': 2, 'python': 2, 'everybody': 1}

# ominiecie problemu braku możliwości przeciązania funkcji
def greet(name="Guest"):
    return f"Hello {name}"


print(greet())  # Hello Guest
print(greet("Radek"))  # Hello Radek


# funkcja przyjmująca args i kwargs
def show_info(*args, **kwargs):
    print(f"Argumenty pozycyjne (args): {args}")
    print(f"Argumenty nazwane (kwargs): {kwargs}")


show_info(1, 2, 3, 4, 5)  # Argumenty pozycyjne (args): (1, 2, 3, 4, 5) - krotka
show_info(a=1, b=8, name="Radek")  # Argumenty nazwane (kwargs): {'a': 1, 'b': 8, 'name': 'Radek'} - słownik


def create_order(client_name=None, *dishes, **extras):
    print(f"Zamowienie dla {client_name}")

    if dishes:
        print("Zamówienie dnia:")
        for dish in dishes:
            print(f" - {dish}")

    else:
        print("Brak zamówionych dań")

    if extras:
        print("\nDodatkowe opcje:")
        for key, value in extras.items():
            print(f" - {key.replace("_", " ").capitalize()}: {value}")
    else:
        print(f"\nBrak dodatkowych opcji")

    print("Zamówienie zostało przyjęte")


create_order("Anna", "Pizza Margerita")
create_order("Tomek", "Pizza Margerita", napoj="Cola")
create_order("Marta", "Burger", "Frytki", "Sałatka")
# Zamowienie dla Anna
# Zamówienie dnia:
#  - Pizza Margerita
#
# Brak dodatkowych opcji
# Zamówienie zostało przyjęte
# Zamowienie dla Tomek
# Zamówienie dnia:
#  - Pizza Margerita
#
# Dodatkowe opcje:
#  - Napoj: Cola
# Zamówienie zostało przyjęte
# Zamowienie dla Marta
# Zamówienie dnia:
#  - Burger
#  - Frytki
#  - Sałatka
#
# Brak dodatkowych opcji
# Zamówienie zostało przyjęte
#
# Process finished with exit code 0

# create_order() # TypeError: create_order() missing 1 required positional argument: 'client_name'
# list, dict, tuple, set
# tuple - niemutowalna lista (krotka)
# frozenset - niemutowalny zbiór - zagnieżdzone sety

a = {1, 2, 3}
b = {4, 5, 6}

# nested = {a, b}  # TypeError: unhashable type: 'set'
# ctrl / - komentarz w linii


a = frozenset({1, 2, 3})
b = frozenset({4, 5, 6})
nested = {a, b}
print(nested)  # {frozenset({1, 2, 3}), frozenset({4, 5, 6})}

books = [
    ("Wiedżmin", "Andrzej Sapkowski", 1990),
    ("Pan Tadeusz", "Adam Mickiewicz", 1834),
    ("Dziady", "Adam Mickiewicz", 1823),
    ("Dziady", "Adam Mickiewicz", 1823),
    ("Lalka", "Bolesław Prus", 1897),
]

print(books)
# [('Wiedżmin', 'Andrzej Sapkowski', 1990), ('Pan Tadeusz', 'Adam Mickiewicz', 1834)]

authors = set()  # tworzenie seta
zbior = {4, 5, 6, 7}
print(type(zbior))  # <class 'set'>

library_by_author = {}  # dict - słownik
print(type(library_by_author))  # <class 'dict'>

opening_hour = ("9:00", "17:00")

print(f"Godziny otwarcia biblioteki: {opening_hour[0]} - {opening_hour[1]}\n")
# Godziny otwarcia biblioteki: 9:00 - 17:00
open_hour, close_hour = opening_hour  # rozpakowannie krotki
print(f"Godziny otwarcia biblioteki: {open_hour} - {close_hour}\n")

# dodanie autorów do zbioru
for title, author, year in books:
    authors.add(author)
    if author not in library_by_author:
        library_by_author[author] = []  # jako wartość dla klucza lista
    library_by_author[author].append((title, year))

print("Unikalni autorzy w bibliotece:")
for author in authors:
    print(f" - {author}")  # f-string - formatownie stringów

# Unikalni autorzy w bibliotece:
#  - Adam Mickiewicz
#  - Andrzej Sapkowski

print("\nKsiązki zawarte w bibliotece")
for title, author, year in books:
    print(f" - '{title}' ({year}), author: {author}")
# Ksiązki zawarte w bibliotece
#  - 'Wiedżmin' (1990), author: Andrzej Sapkowski
#  - 'Pan Tadeusz' (1834), author: Adam Mickiewicz

print("\n Ksiązki wg autorów:")
for items in library_by_author.items():
    print(items)  # ('Adam Mickiewicz', [('Pan Tadeusz', 1834)])

print("\n Ksiązki wg autorów:")
for author, titles in library_by_author.items():
    print(f"\nAuthor: {author}")
    for title, year in titles:
        print(f" -> '{title}' ({year})")
#  Ksiązki wg autorów:
#
# Author: Andrzej Sapkowski
#  -> 'Wiedżmin' (1990
#
# Author: Adam Mickiewicz
#  -> 'Pan Tadeusz' (1834

# https://peps.python.org/pep-0008/
# snake_case
# UpperCamelCase -> PascalCase
# PI - jako stałe
# ctrl alt l - formatowanie kodu do zasad PEP8

# Author: Adam Mickiewicz
#  -> 'Pan Tadeusz' (1834)
#  -> 'Dziady' (1823)
#  -> 'Dziady' (1823)

print("\nWybrane operacje na kolekcjach:")
books.append(("Solaris", "Stanisław Lem", 1961))
print(f'Dodano nową ksiązkę. Liczba ksiązek: {len(books)}\n')
# Wybrane operacje na kolekcjach:
# Dodano nową ksiązkę. Liczba ksiązek: 5
imie = "Radek"
print("Masz na %s" % imie)

print("Masz na imię {}".format(imie))
print("Masz na imie", imie)
# Masz na Radek
# Masz na imię Radek
# Masz na imie Radek

# sprawdzenie czy autor istnieje
author_to_check = "Stanisław Lem"
if author_to_check in authors:
    print(f"Autor {author_to_check} jest już w bibliotece")
else:
    print(f"Dodajemy nowego autora: {author_to_check}")
    authors.add(author_to_check)

print(authors)
# Dodajemy nowego autora: Stanisław Lem
# {'Adam Mickiewicz', 'Stanisław Lem', 'Andrzej Sapkowski'}

# odczytac ksiązki konkretnego autora
author_lookup = "Bolesław Prus"
if author_lookup in library_by_author:
    print(f"\nKsiązki autora: {author_lookup}")
    for title, year in library_by_author[author_lookup]:
        print(f" - '{title}' ({year})")
else:
    print(f"Brak ksiązek autora {author_lookup}")
# Brak ksiązek autora Bolesław Prus
# Ksiązki autora: Bolesław Prus
#  - 'Lalka' (1897)

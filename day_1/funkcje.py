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

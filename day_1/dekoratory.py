# dekorator - przyjmuje funkcje jako argument i modyfikuje, dodaje funkcjonalność
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Przed wywołąniem funkcji")
        return func(*args, **kwargs)

    return wrapper  # zwracamy referencje, adres funkcji


@my_decorator  # użycie dekoratoraa
def hello():
    """To jest oryginalna funkcja hello"""
    print("Hello!")


print(help(hello()))
print(hello.__doc__)  # To jest oryginalna funkcja hello
# pydoc -b - serwer dokumentacji
# pydoc
# pydoc -w .\dekoratory.py
# cd day1 - zmiana katalogu
# cd .. - wyjscie wyżej

print(hello.__name__)
print(hello.__doc__)
# bez dekoratora
# hello
# To jest oryginalna funkcja hello
# po uzyciu dekoratora
# wrapper
# None
# po uzyciu @wraps() wróciło do normy
# hello
# To jest oryginalna funkcja hello

hello()
# Przed wywołąniem funkcji
# Hello!
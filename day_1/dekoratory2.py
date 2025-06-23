# dekorator mierzący czas i  logujący dane
import operator
import time
from functools import wraps, partial


def log_and_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Wywołąnie funkcji: {func.__name__}")
        print(f"[LOG] Argumenty: {args}, Argumenty nazwane: {kwargs}")
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        duration = end_time - start_time
        print(f"[LOG] Wynik: {result}")
        print(f"[LOG] Czas wykonania: {duration:.4f} sekundy")
        return result

    return wrapper


@log_and_time
def compute_sum(a, b):
    time.sleep(1)  # zatrzymanie na 1 s
    return a + b


@log_and_time
def slow_multiply(a, b):
    time.sleep(2)
    return a * b


@log_and_time
def sleep_2s():
    time.sleep(2)


compute_sum(10, 20)  # [LOG] Czas wykonania: 1.0010 sekundy
slow_multiply(a=7, b=8)
#
# [LOG] Wywołąnie funkcji: compute_sum
# [LOG] Argumenty: (10, 20), Argumenty nazwane: {}
# [LOG] Wynik: 30
# [LOG] Czas wykonania: 1.0003 sekundy
#
# [LOG] Wywołąnie funkcji: slow_multiply
# [LOG] Argumenty: (), Argumenty nazwane: {'a': 7, 'b': 8}
# [LOG] Wynik: 56
# [LOG] Czas wykonania: 2.0006 sekundy

sleep_2s()
# [LOG] Wywołąnie funkcji: sleep_2s
# [LOG] Argumenty: (), Argumenty nazwane: {}
# [LOG] Wynik: None
# [LOG] Czas wykonania: 2.0001 sekundy
lista2 = list(range(10_000_000))


@log_and_time
def my_for():
    l = []
    for i in lista2:
        l.append(i * 2)


@log_and_time
def my_for_list_comprehensions():
    l = [i * 2 for i in lista2]


@log_and_time
def my_for_map():
    l_map = list(map(lambda x: x * 2, lista2))

@log_and_time
def my_for_map_operator():
    l_map = list(map(partial(operator.mul, 2), lista2))



my_for()
# [LOG] Wywołąnie funkcji: my_for
# [LOG] Argumenty: (), Argumenty nazwane: {}
# [LOG] Wynik: None
# [LOG] Czas wykonania: 0.0799 sekundy

my_for_list_comprehensions()
# [LOG] Wywołąnie funkcji: my_for_list_comprehensions
# [LOG] Argumenty: (), Argumenty nazwane: {}
# [LOG] Wynik: None
# [LOG] Czas wykonania: 0.0682 sekundy

my_for_map()
# [LOG] Wywołąnie funkcji: my_for_map
# [LOG] Argumenty: (), Argumenty nazwane: {}
# [LOG] Wynik: None
# [LOG] Czas wykonania: 1.0990 sekundy

my_for_map_operator()
# [LOG] Wywołąnie funkcji: my_for_map_operator
# [LOG] Argumenty: (), Argumenty nazwane: {}
# [LOG] Wynik: None
# [LOG] Czas wykonania: 0.8812 sekundy

@log_and_time
def slow_function():
    print("Start slow_function()")
    # time.sleep(1)
    total = 0
    for i in range(1, 1_000_000):
        total += i ** 0.5
    print("End slow_function()")
    return total

@log_and_time
def fast_function():
    print("Start fast_function()")
    total = sum([i ** 0.5 for i in range(1, 1_000_000)])
    print("End fast function()")
    return total

slow_function()
fast_function()
# [LOG] Wywołąnie funkcji: slow_function
# [LOG] Argumenty: (), Argumenty nazwane: {}
# Start slow_function()
# End slow_function()
# [LOG] Wynik: 666666166.4588418
# [LOG] Czas wykonania: 1.1868 sekundy
#
# [LOG] Wywołąnie funkcji: fast_function
# [LOG] Argumenty: (), Argumenty nazwane: {}
# Start fast_function()
# End fast function()
# [LOG] Wynik: 666666166.4588221
# [LOG] Czas wykonania: 0.2133 sekundy
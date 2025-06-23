# dekorator mierzący czas i  logujący dane
import time
from functools import wraps


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


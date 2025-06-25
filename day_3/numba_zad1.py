from numba import jit
import time


@jit(nopython=True)
def numba_sum(n):
    s = 0
    for i in range(n):
        s += i
    return s


def plain_sum(n):
    s = 0
    for i in range(n):
        s += i
    return s


n = 100_000_000

start = time.time()
print("Numba wynik", numba_sum(n))
end = time.time()
print("Czas wykonania:", end - start)

start = time.time()
print("plain wynik", plain_sum(n))
end = time.time()
print("Czas wykonania:", end - start)
# Numba wynik 4999999950000000
# Czas wykonania: 0.6669125556945801
# plain wynik 4999999950000000
# Czas wykonania: 8.197699785232544
import random


def slow_search(lst, target):
    # sposób standardowy
    for i in lst:
        if i == target:
            return True
    return False


def fast_search(s, target):
    return target in s


def main():
    data = list(range(50_000_000))
    target = random.choice(data)
    slow_search(data, target)
    # fast_search(data, target)
    fast_search(set(data), target)


if __name__ == '__main__':
    import cProfile

    cProfile.run('main()', sort='cumtime')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    9.043    9.043 {built-in method builtins.exec}
#         1    0.934    0.934    9.041    9.041 <string>:1(<module>)
#         1    8.026    8.026    8.107    8.107 profilowanie_zad3.py:16(main)
#         1    0.080    0.080    0.080    0.080 profilowanie_zad3.py:4(slow_search)
#         1    0.003    0.003    0.003    0.003 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.001    0.001    0.001    0.001 profilowanie_zad3.py:12(fast_search)
#         1    0.000    0.000    0.000    0.000 random.py:345(choice)
#         1    0.000    0.000    0.000    0.000 random.py:245(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}

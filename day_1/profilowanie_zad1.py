import cProfile


def test_function():
    total = 0
    for i in range(1, 100_000):
        total += i ** 2
    return total


cProfile.run('test_function()')
#          4 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 profilowanie_zad1.py:4(test_function)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0
#          4 function calls in 0.037 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.037    0.037 <string>:1(<module>)
#         1    0.037    0.037    0.037    0.037 profilowanie_zad1.py:4(test_function)
#         1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
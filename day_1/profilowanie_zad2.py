import cProfile
import time


def slow_function():
    print("Start slow_function()")
    time.sleep(1)
    total = 0
    for i in range(1, 1_000_000):
        total += i ** 0.5
    print("End slow_function()")
    return total


def fast_function():
    print("Start fast_function()")
    total = sum([i ** 0.5 for i in range(1, 1_000_000)])
    print("End fast function()")
    return total


def main():
    slow_function()
    fast_function()


cProfile.run("main()")
# End fast function()
#          12 function calls in 1.472 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.472    1.472 <string>:1(<module>)
#         1    0.289    0.289    0.296    0.296 profilowanie_zad2.py:15(fast_function)
#         1    0.000    0.000    1.472    1.472 profilowanie_zad2.py:22(main)
#         1    0.175    0.175    1.176    1.176 profilowanie_zad2.py:5(slow_function)
#         1    0.000    0.000    1.472    1.472 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.006    0.006    0.006    0.006 {built-in method builtins.sum}
#         1    1.001    1.001    1.001    1.001 {built-in method time.sleep}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('main()', filename='profiling_result.prof')
# instalacja snakeviz: pip install snakeviz
# uv pip install snakeviz
# uruchomienie obrazu prof: snakeviz .\profiling_result.prof
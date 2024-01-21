import time
# print(time.ctime())
# # time.sleep(5)
# print(time.time())
# print(time.monotonic())
# print(time.perf_counter())

#1
def calculate_it(f, *args):
    st = time.monotonic()
    res = f(*args)
    stop = time.monotonic()
    t = stop -st
    return (res,t)

#2
from math import factorial                   # функция из модуля math
def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)
def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

funcs = [factorial, factorial_recurrent, factorial_classic]

####################################################################
def for_and_append():  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]

funcs2 = [for_and_append, list_comprehension]
####################################################################
def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result

def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]

def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)

funcs3 = [for_and_append, list_comprehension, list_function]
#####################################################################
def get_the_fastest_func(funcs3, it):
    dct = {}
    for el in funcs3:
        st = time.monotonic()
        el(it)
        dct[el.__name__] = time.monotonic() - st
    return dct

print(get_the_fastest_func(funcs3,range(100_0000)))

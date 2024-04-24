from functools import partial

#1 Использование partial
def send_email(name, addr, text):
    print(name,addr, text)

to_Timur = partial(send_email, "Тимур", "timyrik20@beegeek.ru")
send_an_invitation = partial(send_email, text="Школа BEEGEEK приглашает Вас"
                                              " на новый курс по программированию на языке Python. тутут....")
#2 Простейшие примеры мемоизации результатов выполнения функции
def fib(n):
    cache = {1: 1, 2: 1}
    def fib_rec(n):
        result = cache.get(n)
        if result is None:
            result = fib_rec(n - 2) + fib_rec(n - 1)
            cache[n] = result
        return result
    return fib_rec(n)

import functools

def cached(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        result = cache.get(key)
        if result is None:
            result = func(*args, **kwargs)
            cache[key] = result
        return result
    return wrapper

#3

from functools import lru_cache
import sys
import time

# def return_fir(text):
#     return "".join(sorted(list(text)))
#
# st = time.perf_counter()
# for el in [el.strip() for el in sys.stdin]:
#     print(return_fir(el.strip()))
# print(time.perf_counter()-st)

@lru_cache()

def return_this(text):
    return "".join(sorted(list(text)))

# st = time.perf_counter()
# for el in [el.strip() for el in sys.stdin]:
#     print(return_this(el.strip()))
# print(time.perf_counter()-st)

#4
@lru_cache()

def ways(n):
    if n<=3:
        return 1
    elif n==4:
        return 2
    else:
        return ways(n-1) + ways(n-3) + ways(n-4)

#5
# numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21,
# 73, 88, -11, 16, -22]
# nums_rev = reversed(numbers)
# print(type(nums_rev))
# print(next(nums_rev))
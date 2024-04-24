#1
def get_digits(number: int | float) -> list[int]:
    return list(map(int,str(number).replace(".","")))

#2
def top_grade(grades: dict[str, str| list[int]]) -> dict[str,str|int]:
    return {"name": grades["name"], 'top_grade': max(grades["grades"])}

# print(*top_grade.__annotations__.values())

#3
from collections import deque
def cyclic_shift(numbers: list[int | float], step: int) -> None:
    temp = deque(numbers)
    temp.rotate(step)
    numbers[:] = [c for c in temp]


# # TEST_6:
# numbers = [234, 33, 4, 6, 2, 4, 75, 34, 1, 3, 6, 3, 3]
# cyclic_shift(numbers, 7)
#
# print(numbers)

#4
def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    res={}
    for i in range(len(matrix)):
        res[i+1] = matrix[i]
    return res

# print(*matrix_to_dict.__annotations__.values())

#5
def sandwich(func):
    def wrapper(*args, **kwargs):
        print("---- Верхний ломтик хлеба ----")
        if func(*args, **kwargs ) == None:
            print("---- Нижний ломтик хлеба ----")
        else:
            print("---- Нижний ломтик хлеба ----")
            return func(*args, **kwargs)
    return wrapper

# @sandwich
# def add_ingredients(ingredients):
#     print(' | '.join(ingredients))
#
# add_ingredients(['томат', 'салат', 'сыр', 'бекон'])

#6
def new_print(func):
    def wrapper(*args, **kwargs):
        if kwargs:
            if "sep" in kwargs and "end" in kwargs:
                 kwargs["sep"] = kwargs["sep"].upper()
                 kwargs["end"] = kwargs["end"].upper()
                 func(*map(lambda x: str(x).upper(), args), sep=kwargs['sep'], end=kwargs['end'])
            elif "end" in kwargs and "sep" not in kwargs:
                 kwargs["end"] = kwargs["end"].upper()
                 func(*map(lambda x: str(x).upper(), args), end=kwargs['end'])
            elif "sep" in kwargs and "end" not in kwargs:
                func(*map(lambda x: str(x).upper(), args), sep=kwargs['sep'])
        else:
            func(*map(lambda x: str(x).upper(), args))
    return wrapper

#или вот так
# def new_print(func):
#     def wrapper(*args, sep=' ', end='\n'):
#         func(sep.join(map(str, args)).upper(), end = end.upper())
#     return wrapper

# print = new_print(print)

# print = new_print(print)
#
# print('hi', 'there', end='!')

#7
def do_twice(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@do_twice
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


# @do_twice
# def beegeek():
#     print('beegeek')
#
# beegeek()

#8
def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper


# @reverse_args
# def operation(a, b, name):
#     return a // b + name
# print(operation(10, 90, name=1))

#9
def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), "Функция выполнилась без ошибок"
        except:
            return None, "При вызове функции произошла ошибка"
    return wrapper


# @exception_decorator
# def f(x):
#     return x ** 2 + 2 * x + 1
#
# print(f(7))

#10
def takes_positive(func):
    def wrapper(*args, **kwargs):
        for el in args + tuple(kwargs.values()):
            if not isinstance(el, int):
                raise TypeError
            elif isinstance(el, int) and el<=0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper


# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
# print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#!!!Пример декоратора общего назначения
import functools

#11
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Что-то выполняется до вызова декорируемой функции
        value = func(*args, **kwargs)
        # декорируется возвращаемое значение функции
        # или что-то выполняется после вызова декорируемой функции
        return value
    return wrapper

#12
import functools
def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper

# @square
# def add(a, b):
#     '''прекрасная функция'''
#     return a + b
# print(add(1, 1))
# print(add.__name__)
# print(add.__doc__)

#13
def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return res
        else:
            raise TypeError
    return wrapper
@returns_string
def add(a, b):
    return a + b

# try:
#     print(add(3, 7))
# except TypeError as e:
#     print(type(e))

#14

# TEST_3:
import functools
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}")
        print(f"TRACE: возвращаемое значение {func.__name__}(): {repr(func(*args, **kwargs))}")
        return func(*args, **kwargs)
    return wrapper
@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

# print(beegeek())
# print(beegeek.__name__)
# print(beegeek.__doc__)

#15 Пример царь-декоратора принимающего дополнительные аргументы
def print_symbols(symbol, length):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(symbol * length)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@print_symbols('*', 30)
def add(a, b):
    return a + b

@print_symbols('-', 10)
def mult(a, b):
    return a * b

@print_symbols('=', 40)
def diff(a, b):
    return a - b

# print(add(3, 9))
# print(mult(10, 20))
# print(diff(100, 1))

#16
def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return func(*args, **kwargs)+ string
            else:
                return string + func(*args, **kwargs)
        return wrapper
    return decorator

@prefix('online-school ')
def make_lower(string, lower=True):
    '''makes string upper or lower'''
    if lower:
        return string.lower()
    return string.upper()

# print(make_lower.__name__)
# print(make_lower.__doc__)
# print(make_lower('beegeek', False))

#17

import functools
def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
                return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return wrapper
    return decorator


@make_html('i') ## функция Обертывается снизу вверх
@make_html('del')
def get_text(text):
    return text

# print(get_text(text='decorators are so cool!'))

#18
def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                res = func(*args, **kwargs)
            return res

        return wrapper

    return decorator

@repeat(10)
def add(a, b):
    '''sum of two numbers'''
    return a + b


# print(add.__name__)
# print(add.__doc__)
# print(add(10, b=20))

#19

def strip_range(start: int, end: int, char= "."):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                tmp = list(args[0])
            else:
                tmp=list(func())
            for i in range(start, end if len(tmp)>end else len(tmp)):
                tmp[i] = char
            if kwargs:
                tmp.append(kwargs["end"])
            return "".join(tmp)

        return wrapper

    return decorator



# @strip_range(0, 1)
# def beegeek(word, end=" "):
#     """This is... Requiem. What you are seeing is indeed the truth"""
#     return word + end
#
# print(beegeek("beegee", end="k"))
# print(beegeek.__name__)
# print(beegeek.__doc__)

#20

import functools
from datetime import date

def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, datatype):
                return res
            else:
                raise TypeError

        return wrapper

    return decorator

@returns(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

# print(append_this.__name__)
# print(append_this.__doc__)
# print(append_this([1, 2, 3], elem=4))

#21

def takes(*args1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args2, **kwargs):
            for el in args2 + tuple(kwargs.values()):
                if type(el) not in args1:
                    raise TypeError
            return (func(*args2, **kwargs))

        return wrapper

    return decorator


@takes(str)
def beegeek(word, repeat):
    return word * repeat

# try:
#     print(beegeek('beegeek', repeat=2))
# except TypeError as e:
#     print(type(e))

#22

def add_attrs(**kwargs):
    def decorator(func):
        for k, v in kwargs.items():
            setattr(func, k, v)
        @functools.wraps(func)
        def wrapper(*args, **kwargs1):
            return func(*args, **kwargs1)

        return wrapper

    return decorator


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'

#
# print(beegeek.attr1)
# print(beegeek.attr2)

import functools

#23
def ignore_exception(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args1, **kwargs2):
            try:
                return func(*args1, **kwargs2)
            except Exception as err:
                if type(err) in args:
                    print(f"Исключение {type(err).__name__} обработано")
                else:
                    raise err

        return wrapper

    return decorator

@ignore_exception()
def func():
    '''func docs'''
    raise ValueError

# try:
#     func()
# except Exception as e:
#     print(type(e))

#24

import functools
class MaxRetriesException(Exception):
    pass

def retry(times: int):

    def decorator(func):
        tmp = times
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass
            else:
                raise MaxRetriesException
        return wrapper

    return decorator

@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')

# beegeek()
#1
def traffic(n):
    if n > 0:
        print('Не парковаться')
        traffic(n - 1)

#2
def test(st):
    if st <= 100:
        print(st)
        test(st + 1)

# test(1)

#3
numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341,
           437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331,
           323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127,
           984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777,
           805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]

def show_el(st):
    if st < len(numbers):
        print(f"Элемент {st}: {numbers[st]}")
        show_el(st + 1)

# show_el(0)

#4
import sys

# data = [el.strip() for el in sys.stdin]
# data = data[:data.index("0") + 1]

# def show_el(st):
#     if st >= -len(data):
#         print(data[st])
#         show_el(st - 1)

# show_el(-1)

#Изящное решение
def func():
    n = int(input())
    if n:
        func()
    print(n)

#5
def triangle(st):
    if st > 0:
        print(st * "*")
        triangle(st - 1)

#6
def triangle(st):
    if st > 0:
        triangle(st - 1)
        print(st * "*")

#7
def piram(st,mult):
    if st <= 4:
        if f"{(str(st) * mult)}" == '4444':
            pass
        else:
            print(f"{(str(st) * mult).center(16)}")
            piram(st + 1, mult-4)
        print(f"{(str(st) * mult).center(16)}")

# piram(1, 16)

#8
def print_digits(num):
    if num:
        print(list(str(num))[-1])
        num = "".join(list(str(num))[:-1])
        print_digits(num)

# print_digits(12345)

#9
def print_digits_reverse(num):
    if num:
        print(list(str(num))[0])
        num = "".join(list(str(num))[1:])
        print_digits(num)

# print_digits(12345)

#10
x = 17488
def lenght(x, summ):
    if x<10:
        summ+=1
        print(summ)
    else:
        x//=10
        summ+=1
        lenght(x,summ)

# lenght(x,0)

#11
x = 174
def lenght(x, summ):
    if x<10:
        summ+=x
        print(summ)
    else:
        summ += x%10
        x//=10
        lenght(x,summ)

# lenght(x,0)

#12
def number_of_frogs(year):
    if year==1:
        return 77
    else:
        return 3*(number_of_frogs(year-1)-30)

# print(number_of_frogs(3))

#13
def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    else:
        return numbers[start] + range_sum(numbers, start + 1, end)

#14
def get_pow(a,n):
    if n == 0:
        return 1
    else:
        return a * get_pow(a,n-1)

# print(get_pow(5, 2))

#15
def get_fast_pow(a,n):
    if n == 0:
        return 1
    elif n%2 == 0:
        return get_fast_pow(a, n / 2) * get_fast_pow(a, n / 2)
    else:
        return a * get_fast_pow(a,n-1)

# print(get_fast_pow(99, 99))

#16
lst1 =[]
def recursive_sum(a,b):
    if a!=0:
        return 1 + recursive_sum(a-1, b)
    if b!=0:
        return 1 + recursive_sum(a, b-1)
    return sum(lst1)

# print(recursive_sum(10, 22))

#17
def is_power(a):
    if a<2:
        return True
    elif a%2 != 0:
        return False
    return is_power(a//2)

# print(is_power(17))

#18
cache = {1: 1, 2: 1, 3: 1}                # ключ - номер числа, значение - число Фибоначчи
def tribonacci(n):
    result = cache.get(n)
    if result is None:
        result = tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)
        cache[n] = result
    return result

#19
def is_palindrome(st):
    if len(st) in (0,1):
        return True
    else:
        if st[0]!=st[-1]:
            return False
        return is_palindrome(st[1:-1])

#20
def to_binary(x):
    if x in (0,1):
        return (0,1)[x]
    else:
        return "" + str(to_binary(x//2)) + str(x%2)
# print(to_binary(256))

#21
def plus_minus_5(n):
    print(n)
    if n>0:
        plus_minus_5(n-5)
        print(n)
#
# plus_minus_5(16)

#22 Хороший пример обхода любой древовидной структуры с неизвестными количеством эдементов и уровнем вложенности
def get_all_str(data):
    if type(data) == str:
        print(data, end=' ')            # базовый случай
    if type(data) == list:
        for i in data:
            get_all_str(i)              # рекурсивный случай

# numbers = ['1', ['2', '3', ['4'], ['5', ['6', '7']]]]
#
# get_all_str(numbers)

#23
def recursive_sum(data):
    total = 0
    if type(data) == int:
        total+=data
    if type(data) == list:
        for i in data:
            total+=recursive_sum(i)
    return total

# my_list = [1, [4, 4], 2, [1, [2, 10]]]
#
# print(recursive_sum(my_list))

#24
def linear(li):
    new_list = []
    for elem in li:
        if isinstance(elem, list):
            new_list.extend(linear(elem))
        else:
            new_list.append(elem)
    return new_list


# my_list = [3, [4], [5, [6, [7, 8]]]]
# print(linear(my_list))

#25
def get_value(nested_dicts, key):
    if key in nested_dicts:
        res = nested_dicts[key]
        return res
    else:
        for v in nested_dicts.values():
            if type(v) == dict:
                value = get_value(v, key)
                if value is not None:
                    return value


# data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993},
#         'address': {'streetAddress': 'Часовая 25, кв. 127', 'city':
#             {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}
#
# print(get_value(data, 'cityName'))

#26
def get_all_values(nested_dicts, key):
    res = set()
    if key in nested_dicts:
        res.add(nested_dicts[key])
    for v in nested_dicts.values():
        if type(v) == dict:
            value = get_all_values(v, key)
            res.update(value)

    return res

# или такой вариант
# def get_all_values(nested_dicts, key, res=()):
#     res=set()
#     for k,v in nested_dicts.items():
#         if key in nested_dicts:
#             res.add(nested_dicts[key])
#         if type(v)==dict:
#             res.update(get_all_values(v,key))
#     return res

# my_dict = {
#            'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
#            'Timur': {'hobby': 'math'},
#            'Dima': {
#                    'hobby': 'CS',
#                    'sister':
#                        {
#                          'name': 'Anna',
#                          'hobby': 'TV',
#                          'age': 14
#                        }
#                    }
#            }
# result = get_all_values(my_dict, 'hobby')
# print(*sorted(result))

#27

def dict_travel(data, new_str = ""):

    for k,v in sorted(data.items()):
        if isinstance(v,dict):
            dict_travel(v, new_str + f'{k}.')
        else:
            print(f'{new_str}{k}: {v}')



data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)
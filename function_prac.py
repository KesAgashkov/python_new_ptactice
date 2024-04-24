from string import ascii_uppercase
# for el in ascii_uppercase:
#     print(ord(el))

#1
def convert(x):
    return (bin(x)[2:], oct(x)[2:], hex(x)[2:].upper()) if x>=0\
        else ("-" + bin(x)[3:], "-" +  oct(x)[3:], "-" + hex(x)[3:].upper())

# print(convert(-24))

#2
films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
         'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
         'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
         'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
         'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
         'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
         'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
         'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
         'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
         'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}

# print(min(films.items(), key = lambda x: x[1]["imdb"] + x[1]["kinopoisk"])[0])

# print(min(films, key=lambda x: films[x]['imdb'] + films[x]['kinopoisk']))

#3
def non_negative_even(numbers):
    return all([x%2==0 and x>=0 for x in numbers])

# print(non_negative_even([0, 2, -4, 8, 16]))

#4
def is_greater(lsts, num):
    return any([sum(el)>num for el in lsts])

# data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
# print(is_greater(data, 10))

#5
def custom_isinstance(lst, num):
    return len([el for el in lst if isinstance(el,num)])

# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, int))

#6
def my_pow(num):
    res = 0
    for el in enumerate(list(num),1):
        res+=pow(int(el[1]),el[0])
    return res

# print(my_pow("139"))

#7
names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

# for name, bud, box in sorted(zip(names, budgets, box_offices)):
#     print(f"{name}: {box-bud}$")

#8
def zip_longest(*args, fill=None):
    new = []
    max_len=len(max(args,key=len))
    for ls in args:
        l =max_len-len(ls)
        ls.extend(l * [fill])

    return list(zip(*args))

# print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c']))

#9
def strange_sort(st):
    low, up, odd, even = [],[],[],[]
    for el in st:
        if el.isalpha():
            if el.islower():
                low.append(el)
            else:
                up.append(el)
        elif el.isdigit():
            if int(el)%2!=0:
                odd.append(el)
            else:
                even.append(el)
    print("".join(sorted(low)) + "".join(sorted(up)) + "".join(sorted(odd)) + "".join(sorted(even)))


#Решение от представителей внеземных цивилизаций
from string import ascii_letters
# pattern = ascii_letters + '1357902468'
# print(''.join(sorted(input(), key=pattern.index)))


# strange_sort("Sorting1234")
#10
def hash_as_key(objects):
    dct = {}
    for el in objects:
        dct.setdefault(hash(el), []).append(el)
    for k,v in dct.items():
        if len(v)==1:
            dct[k]=v[0]
    return dct

# или так
# def hash_as_key(data):
#     d = {}
#     for i in data:
#         d.setdefault(hash(i), []).append(i)
#     return {k: v[0] if len(v) == 1 else v for k, v in d.items()}
#
# data = [1, 2, 3, 4, 5, 5]
#
# print(hash_as_key(data))

#11
def use_eval():
    seq = eval(input())
    print(seq[-1] if type(seq) == list else seq[0] if type(seq) == tuple else len(seq))

#12
import sys
def use_eval_2():
    print(max([eval(el) for el in sys.stdin]))

# Sample Input 2:
# 1 + 1 + 1 + 1 + 1
# 2 * 2 * 2 * 2 * 2
# 3 // 3 // 3 // 3 // 3
# 4 - 4 - 4 - 4 -4

#13
def search_max_min_func():
    lst = []
    equa = input()
    inter = tuple(map(int, input().split(" ")))
    for i in range(inter[0], inter[1] + 1):
        lst.append(eval(equa.replace("x", f'({str(i)})')))

    print(f'Минимальное значение функции {equa} на отрезке [{inter[0]}; {inter[1]}] равно {min(lst)}')
    print(f'Максимальное значение функции {equa} на отрезке [{inter[0]}; {inter[1]}] равно {max(lst)}')

# Sample Input 2:
# x + 1
# -999 999

#14
data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976,
        -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733,
        'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431,
        170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288,
        None, -708.3036176571618]

# print(*map(int, filter(lambda x: isinstance(x, (int,float)), data)), sep="\n")

#15
numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275,
           1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556,
           -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396, 2842,
           -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304,
           4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862,
           2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69,
           96, 1111]

# print(*(el**2 for el in numbers if el%9==0 and len(str(abs(el))) == 2))

#16

names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита',
         'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём',
         'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия',
         'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр',
         'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей',
         'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина',
         'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен',
         'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур',
         'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав',
         'Леонид']

# print(*sorted(map(lambda x: x.title(),filter(lambda x: x.upper().startswith(('М','А')) and len(x)>4, names))))

#17
def print_operation_table(*args):
    if "<lambda>" in str(args):
        lst = [[i*j for i in range(1,args[-2]+1)] for j in range(1,args[-1]+1)]
    else:
        lst = [[args[0](j,i) for i in range(1,args[-1]+1)] for j in range(1, args[-2]+1)]

    for i in range(args[-2]):
        for j in range(args[-1]):
            print(str(lst[i][j]).ljust(3), end=' ')
        print()

#или вот так
# print_operation_table = lambda operation, rows, cols: [print(*[operation(i, j) for j in range(1, cols+1)])
#                                                        for i in range(1, rows+1)]

from operator import mul

# print_operation_table(pow, 5, 10)

#18
from string import ascii_lowercase, ascii_uppercase
def verification(login, password, success, failure):
    low, up, numb = False,False,False
    for el in password:
        if el in ascii_lowercase:
            low = True
        if el in ascii_uppercase:
            up = True
        if el.isdigit():
            numb = True
    if all([low, up, numb]):
        return success(login)
    else:
        if not low and not up:
            return failure(login, "в пароле нет ни одной буквы")
        elif not up:
            return failure(login, "в пароле нет ни одной заглавной буквы")
        elif not low:
            return failure(login, "в пароле нет ни одной строчной буквы")
        elif not numb:
            return failure(login, "в пароле нет ни одной цифры")

def success(login):
    print(f'Здравствуйте, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')

# verification('Arthur_Davletov', 'мойпароль123', success, failure)

#19
def numbers_sum(elems):
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    """
    return sum([el for el in elems if isinstance(el, (int,float))])
#
# print(numbers_sum.__doc__)

#20
old_print = print
def print(*args,**kwargs):
     res = tuple(el.upper() if isinstance(el,str) else el for el in args)
     if kwargs:
         if "sep" in kwargs:
             kwargs["sep"] = kwargs["sep"].upper()
         if "end" in kwargs:
             kwargs["end"] = kwargs["end"].upper()
         return old_print(*res, sep=kwargs['sep'], end=kwargs['end'])
     else:
         return old_print(*res)

# print('beegeek', [1, 2, 3], 4)

#21
def polynom(x):
    res = x**2+1
    if not hasattr(polynom, 'values'):
        polynom.values = set()
    polynom.values.add(res)
    return res

# polynom(1)
# polynom(2)
# polynom(3)
# print(*sorted(polynom.values))

#22

def remove_marks(text, marks):
    if not hasattr(remove_marks, 'count'):
        remove_marks.count = 0
    remove_marks.count += 1
    for char in marks:
          text = text.replace(char, "")
    return text

# text = 'Hi! Will we go together?'
#
# print(remove_marks(text, '!?'))
# print(remove_marks.count)

#23 Пример простого замыкания
def power(degree):
    def inner(x):
        return x**degree
    return inner

# square = power(2)
# print(square(5))

#24 еще одна простая реализация
def generator_square_polynom(a,b,c):
    def inner(x):
        return a*(x**2)+b*x+c
    return inner

# f = generator_square_polynom(1, 2, 1)
# print(f(5))

def sourcetemplate(url):
    def inner(**kwargs):
        st = url.split("?")[0]+ "?"
        for k,v in sorted(kwargs.items()):
            st+=str(k)+"="+str(v)+"&"
        return st[:-1]
    return inner

# url = 'https://all_for_comfort_life.com'
# load = sourcetemplate(url)
# print(load(smartphone='iPhone', notebook='huawei', sale=True))

from datetime import datetime,date

def date_formatter(country_code):
    d = {'ru': '%d.%m.%Y',
     'us': '%m-%d-%Y',
     'ca': '%Y-%m-%d',
     'br': '%d/%m/%Y',
     'fr': '%d.%m.%Y',
     'pt': '%d-%m-%Y',}
    def inner(date):
        return datetime.strftime(date, d[country_code])
    return inner

# date_ru = date_formatter('us')
# today = date(2025, 1, 5)
# print(date_ru(today))

def sort_priority(values, group):
    m1 = max(group)
    m2 =max(values)

    values.sort(key=lambda x: x if x in group else x+ m1 + m2)

numbers = list(range(100, -100, -1))
sort_priority(numbers, (98, 97, 100, 5, -9, -34))

print(numbers)

[-34, -9, 5, 97, 98, 100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81,
 -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57,
 -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -33, -32,
 -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -8, -7, -6,
 -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
 91, 92, 93, 94, 95, 96, 99]

print(0 + 'python')
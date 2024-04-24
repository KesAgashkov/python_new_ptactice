#1
def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    return filter(lambda x: not predicate(x), iterable)

# numbers = [1, 2, 3, 4, 5]
#
# print(*filterfalse(lambda x: x >= 3, numbers))

#2
def transpose(matrix):
    tmp = list(zip(*matrix))
    matrix = []
    for i in range(len(tmp)):
        matrix.append(list(tmp[i]))
    return matrix

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# for row in transpose(matrix):
#     print(row)

#3
def get_min_max(data):
    if data:
        return data.index(min(data)), data.index(max(data))

# data = [2, 3, 8, 1, 7]
#
# print(get_min_max(data))

#4

def starmap(func, iterable):
    return map(func, *zip(*iterable))

# points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]
#
# print(*starmap(lambda x, y, z: x * y * z, points))

import copy
def get_min_max(iterable):
    iterable = iter(iterable)
    min, max = 0, 0
    try:
        tmp = next(iterable)
        min = tmp
        max = tmp
        for el in iterable:
            if min>el:
                min=el
            if max<el:
                max=el
        return min,max
    except:
        return None

# iterable = iter([])
#
# print(get_min_max(iterable))

# print(dir(iter([1,2,3])))
# for el in iter (int,0):
#     print(el)

#5
def is_iterable(obj):
    return  True if '__iter__' in dir(obj) else False

#6

from random import randint
def random_numbers(l,r):
    return iter(lambda: randint(l, r), -1)

#7

class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj

# geek = Repeater('geek')
# print(next(geek))
# print(next(geek))
# print(next(geek))

#8

class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.times==0:
            raise StopIteration
        else:
            self.times-=1
            return self.obj

# geek = BoundedRepeater('geek', 3)
#
# print(next(geek))
# print(next(geek))
# print(next(geek))
#
# try:
#     print(next(geek))
# except StopIteration:
#     print('Error')

#9

class Square:
    def __init__(self, n):
        self.n = n
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.n:
            raise StopIteration
        else:
            self.start += 1
            return self.start ** 2

# squares = Square(10)
#
# print(list(squares))

#10

class Fibonacci:
    def __init__(self):
        self.one = 1
        self.two = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.one, self.two = self.two, self.one + self.two
        return self.two

# fibonacci = Fibonacci()
#
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))

#11

class PowerOf:
    def __init__(self, number):
        self.number = number
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self.number ** self.start
        self.start += 1
        return res

# power_of_two = PowerOf(2)
#
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))

#12
class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.sigh = list(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        else:
            self.index += 1
            return self.sigh[self.index-1],self.data[self.sigh[self.index-1]]

# pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
#
# print(*pairs)

#13

class CardDeck:
    def __init__(self):
        self.cards = [f'{j} {i}' for i in ("пик", "треф", "бубен", "червей") for j in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.cards)-1:
            raise StopIteration
        else:
            self.index+=1
            return self.cards[self.index]


# cards = list(CardDeck())
#
# print(cards[9])
# print(cards[23])
# print(cards[37])
# print(cards[51])

#14
class Cycle:

    def __init__(self, obj):
        self.obj = obj
        self.it = iter(self.obj)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.it)
        except StopIteration:
            self.it = iter(self.obj)
            return next(self.it)


# cycle = Cycle(range(100_000_000))
# print(next(cycle))
# print(next(cycle))

#15

from random import choice
class RandomNumbers:

    def __init__(self, left, right, n):
        self.ran = range(left,right+1)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return choice(self.ran)


# iterator = RandomNumbers(-1000, -900, 1)
#
# print(next(iterator) in range(-1000, -899))
#
# try:
#     next(iterator)
# except StopIteration:
#     print('Error')

#16

import string

class Alphabet:
    alpha = {
        "en": string.ascii_lowercase,
        "ru": "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    }

    def __init__(self, language):
        self.iterable = Alphabet.alpha[language]
        self.iterator = iter(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
        return next(self.iterator)

# en_alpha = Alphabet('en')
#
# letters = [next(en_alpha) for _ in range(30)]
#
# print(*letters)

# en_alpha = Alphabet('en')
#
# for _ in range(100):
#     print(next(en_alpha))

from math import floor
class Xrange:
    def __init__(self, start, end, step=1):
        if isinstance(step,int) and isinstance(start, int) and isinstance(end, int):
            self.iterator = iter(range(start,end,step))
        else:
            if step > 0:
                lst = [start]
                for _ in range(floor((end - start) // step)):
                    if (end - step) <= start:
                        break
                    lst.append(start + step)
                    start += step
                self.iterator = iter(lst)
            else:
                lst = [start]
                for _ in range(abs(floor((start - end) // step))):
                    if end + abs(step) >= start:
                        break
                    lst.append(start + step)
                    start += step
                self.iterator = iter(lst)
    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except:
            raise StopIteration


# xrange = Xrange(0, 3, 0.5)
#
# print(*xrange, sep='; ')








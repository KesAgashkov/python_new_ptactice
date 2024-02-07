import sys
import json
#1
def exs_1():
    tot, count = 0, 0
    for item in [el.strip() for el in sys.stdin]:
        try:
            item = float(item)
            tot +=item
        except ValueError:
            count+=1
    print(int(tot) if ".0" in str(tot) else tot, count, sep="\n")

#2
def add_to_list_in_dict(data, key, element):
    try:
        data[key].append(element)
    except:
        data[key] = [element]

# data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# add_to_list_in_dict(data, 'c', 7)
# print(data)

#3

week = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
def get_weekday(n):
    if not isinstance(n,int):
        raise TypeError('Аргумент не является целым числом')
    elif n not in range(1, 8):
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return week[n]

#
# try:
#     print(get_weekday(4.0))
# except Exception as err:
#     print(err)
#     print(type(err))

#4
def get_id(names, name):
    if type(name) != str:
        raise TypeError('Имя не является строкой')
    elif not name.istitle() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    else:
        return len(names)+1

# names = ['Timur', 'Anri', 'Dima', 'Arthur']
# name = 'Ruslan1337'
#
# try:
#     print(get_id(names, name))
# except ValueError as e:
#     print(e)

#5
def safe_load_json():
    try:
        file = open(input(), "r")
        try:
            print(json.load(file))
        except:
            print("Ошибка при десериализации")
    except:
        print("Файл не найден")

#6
class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass
def is_good_password(x):
    if not len(x)>=9:
        raise LengthError
    elif x.isdigit() or not([el for el in x if el.islower()] and [el for el in x if el.isupper()]):
        raise LetterError
    elif not [el for el in x if el.isdigit()]:
        raise DigitError
    else:
        return True

#7
def check_pass():
    for x in [el.strip() for el in sys.stdin]:
        if not len(x)>=9:
            print("LengthError")
        elif x.isdigit() or not([el for el in x if el.islower()] and [el for el in x if el.isupper()]):
            print("LetterError")
        elif not [el for el in x if el.isdigit()]:
            print("DigitError")
        else:
            print("Success!")
            break

# arr1
# Arrrrrrrrrrr
# arrrrrrrrrrrrrrr1
# Arrrrrrr1
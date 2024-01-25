from collections import namedtuple

#1 Создание класса namedtuple
Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])

#2 Создание расширенного класса namedtuple
Game = namedtuple('Game', 'name developer publisher')
ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])


#3
def anima():
    Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

    data = [Animal(name='Alex', family='dogs', sex='m', color='brown'), Animal(name='Nancy', family='dogs', sex='w', color='black')]
    for el in data:
        tmp = el
        for f,v in zip(el._fields, el):
            print(f'{f}: {v}')
        print()

#4
def add_new_func():
    User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

    users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
             User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
             User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
             User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
             User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
             User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
             User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
             User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
             User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
             User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
             User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
             User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
             User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
             User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
             User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

    for el in sorted(users, key=lambda x: (('Gold', 'Silver', 'Bronze', 'Basic').index(x.plan), x.email)):
        print(el.name, el.surname)
        print(f"  Email: {el.email}")
        print(f"  Plan: {el.plan}")
        print()

#5
from datetime import datetime
import csv
def onemore_sort():
    with open("csv/meetings.csv", encoding="UTF-8") as file:
        data = {(el[2] + " " + el[3]): (el[0], el[1]) for el in csv.reader(file)}
        del data["meeting_date meeting_time"]
        data = {datetime.strptime(k, "%d.%m.%Y %H:%M"):v for k,v in data.items()}
        for k,v in sorted((data.items())):
            print(v[0], v[1])



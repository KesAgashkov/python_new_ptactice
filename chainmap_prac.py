import sys
from collections import ChainMap
from collections import Counter
import json

#1
def format_task():
    bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
    meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
    sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
    vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
    toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

    chm = ChainMap(bread,meat,sauce,vegetables,toppings)
    lst = input().split(",")
    sp = Counter(lst)
    l1 = len(max(sp, key=len))
    l2 = len(str((max(sp.items(), key=lambda x: len(str(x[1])))[1])))

    for el in sorted(sp):
        print(f"{el.ljust(l1)} x {sp[el]}")

    tot = f'ИТОГ: {sum([chm[el] for el in lst])}'

    if (l1+3+l2) >= len(tot):
        print("-"*(l1+2+l2))
    else:
        print("-" * (len(tot)))

    print(tot)

#2
def get_all_values(chainmap, key):
    res = set()
    for el in chainmap.maps:
        try:
            res.add(el[key])
        except KeyError:
            pass
    return res

# chainmap = ChainMap()
# result = get_all_values(chainmap, 'age')
# print(*sorted(result))

#3
def deep_update(chainmap, key, value):
    if key in chainmap:
        for dct in chainmap.maps:
            if key in dct:
                dct[key] = value
    else:
        chainmap.maps[0].update({key: value})

# chainmap = ChainMap({})
# deep_update(chainmap, 'city', 'Moscow')
# print(chainmap)

#4
def get_value(chainmap, key, from_left=True):
    if key in chainmap:
        if from_left:
            return chainmap[key]
        else:
            chainmap.maps.reverse()
            return chainmap[key]

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))
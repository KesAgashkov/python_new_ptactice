from collections import OrderedDict
#1
def sort_orddict():
    data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                        'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                        'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

    print(OrderedDict(reversed(data.items())))


data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
                    'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
                    'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, '
                                                          'дом 6/2', 'SeatsCount': '10'})

def sad_task():
    data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                        'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва,'
                        ' переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
    new = OrderedDict()
    for el in [False if i % 2 == 0 else True for i in range(len(data))]:
        tmp = data.popitem(last=el)
        new[tmp[0]] = tmp[1]
    print(new)

def custom_sort(ordered_dict, by_values=False):
    if by_values:
        for el in (sorted(ordered_dict.items(), key=lambda x: x[1])):
            ordered_dict.move_to_end(el[0])
    else:
        for el in (sorted(ordered_dict.items(), key=lambda x: x[0])):
            ordered_dict.move_to_end(el[0])

# data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
# custom_sort(data)
# print(data)




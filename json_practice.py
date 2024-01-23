#1
import json
import sys
import csv
from datetime import time, datetime
def exs_1():
    countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
                 'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
                 'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
                 'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

    json_data = json.dumps(countries, indent=3,  separators=(',', ' - '), sort_keys=True)
    print(json_data)

#2
def exs_2():
    words = {
             frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
             "travel": "trævl",
             ("hello", "world"): ("həˈləʊ", "wɜːld"),
             "moonlight": "muːn.laɪt",
             "sunshine": "ˈsʌn.ʃaɪn",
             ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
             "adventure": "ədˈventʃər",
             "beautiful": "ˈbjuːtɪfl",
             frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
             "bicycle": "baisikl",
             ("pilot", "fly"): ("pailət", "flai")
            }
    json_data = json.dumps(words, skipkeys=True)
    print(json_data)
#3
def exs_3():
    club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
             "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

    club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
             "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

    club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
             "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

    with open("jsons/data.json", "w", encoding="utf-8") as file:
        json.dump([club1,club2,club3],file, indent=3)
#4
def exs_4():
    specs = {
             'Модель': 'AMD Ryzen 5 5600G',
             'Год релиза': 2021,
             'Сокет': 'AM4',
             'Техпроцесс': '7 нм',
             'Ядро': 'Cezanne',
             'Объем кэша L2': '3 МБ',
             'Объем кэша L3': '16 МБ',
             'Базовая частота': '3900 МГц'
            }

    specs_json = json.dumps(specs, ensure_ascii=False, indent=3)

    print(specs_json)

#5
def is_correct_json(data):
    try:
        data = json.loads(data)
        return True
    except ValueError:
        return False

# print(is_correct_json('{"name"= "Barsik", "age": 7, "meal": "Wiskas"}'))

#6
def exs_6():
    data = json.loads(sys.stdin)
    for k, v in data.items():
        if type(v) == list:
            print(f"{k}: {', '.join(map(str,v))}")
        else:
            print(f"{k}: {v}")

#7
def differ_data_to_json():
    with open("jsons/data.json",encoding="utf-8") as file:
        data = json.load(file)
        data = [el for el in data if el is not None]
        for i in range(len(data)):
            if type(data[i]) == str:
                data[i] += "!"
            elif type(data[i]) == bool:
                data[i] = not(data[i])
            elif type(data[i]) == int:
                data[i]+=1
            elif type(data[i]) == list:
                data[i] += data[i]
            elif type(data[i]) == dict:
                data[i].update({"newkey": None})

    with open ("jsons/updated_data.json", "w", encoding="utf-8") as file_out:
        json.dump(data, file_out, indent=3)

#8
def json_merge():
    with open("jsons/data1.json", encoding="utf-8") as j1, open("jsons/data2.json", encoding="utf-8") as j2:
        fir = json.load(j1)
        sec = json.load(j2)
        fir.update(sec)
    with open ("jsons/data_merge.json", "w", encoding="utf-8") as file_out:
        json.dump(fir, file_out, indent=3)

# json_merge()

#9
def add_extra_fileds():
    with open("jsons/people.json", encoding="utf-8") as p, open("jsons/updated_people.json", "w", encoding="utf-8") as file_out:
         data = json.load(p)
         max_el = max(data,key=len)
         for el in data:
             for k,v in max_el.items():
                 el[k] = el.get(k, None)
    with open("jsons/updated_people.json", "w", encoding="utf-8") as file_out:
        json.dump(data, file_out, indent=3)

#10
def group_by_religion():
    res = {}
    with open("jsons/countries.json", encoding="utf-8") as c, open("jsons/religion.json", "w", encoding="utf-8") as file_out:
        data = json.load(c)
        for el in data:
            res.setdefault(el["religion"], []).append(el["country"])
        json.dump(res,file_out,indent=3)

#11
def crate_hard_dict():
    res = {}
    with open("csv/playgrounds.csv", encoding="UTF-8") as c, open("jsons/addresses.json", "w", encoding="UTF-8") as file_out:
        data = [el for el in csv.reader(c, delimiter=";")]
        data.pop(0)
        for el in data:
            res.setdefault(el[1], {}).setdefault(el[2], []).append(el[3])
        json.dump(res, file_out, indent=3, ensure_ascii=False)

#12
def json_to_csv():
    with open("jsons/students.json", encoding="UTF-8") as pools, open("csv/data.csv", "w", encoding="UTF-8", newline="") as file_out:
        data = [el for el in json.load(c) if el["age"]>=18 and el["progress"]>=75]
        print(data)
        writer = csv.writer(file_out)
        writer.writerow(["name", "phone"])
        for el in sorted(data, key = lambda x: x["name"]):
            print(el)
            writer.writerow([el["name"], el["phone"]])

#13
def search_perfect_pool():
    with open("jsons/pools.json", encoding="UTF-8") as pools:
        data = [el for el in json.load(pools)]
        res = []
        # print(data)
        for el in data:
            times = el["WorkingHoursSummer"]["Понедельник"].split("-")
            begin = datetime.strptime(times[0], "%H:%M")
            stop = datetime.strptime(times[1], "%H:%M")
            if datetime(1900,1,1,10,0) >= begin and stop>=datetime(1900,1,1,12,0):
                res.append(el)
        preres = max(res, key=lambda x: (x["DimensionsSummer"]["Length"],x["DimensionsSummer"]["Width"]))
        print(f'{preres["DimensionsSummer"]["Length"]}x{preres["DimensionsSummer"]["Width"]}')
        print(f'{preres["Address"]}')

#14
def hard_task():
    res= {}
    with open("csv/exam_results.csv", encoding="UTF-8") as score, open("jsons/best_scores.json", "w", encoding="UTF-8", newline="") as file_out:
        head, *data = [el for el in csv.reader(score, delimiter=",")]
        for el in data:
            tmp = [datetime.strptime(el[3], "%Y-%m-%d %H:%M:%S")]
            tmp.extend(el[0:3])
            res.setdefault(el[4], []).append(tmp)
        res = {k: max(v, key=lambda x: (x[3], x[0])) for k,v in res.items()}
        final = []
        for k, v in sorted(res.items()):
            t = v[0].strftime("%Y-%m-%d %H:%M:%S")
            final.append({"name":v[1], "surname":v[2], "best_score":int(v[3]), "date_and_time":t, "email":k})
        json.dump(final, file_out, indent=3)
# hard_task()

#15
def search_max_shops():
    dictrict = {}
    net = {}
    with open("jsons/food_services.json", encoding="UTF-8") as f:
        data = json.load(f)
        for el in data:
            dictrict.setdefault(el["District"], []).append(el["Name"])
            if el["OperatingCompany"] != "":
                net.setdefault(el["OperatingCompany"], []).append(el["Name"])
        # for el,k in dictrict.items():
        #     print(el,len(k))
        preres1 = max(dictrict, key=lambda x: len(dictrict[x]))
        preres2 = max(net, key=lambda x: len(net[x]))
        print(f"{preres1}: {len(dictrict[preres1])}")
        print(f"{preres2}: {len(net[preres2])}")

search_max_shops()

#16

def search_bigger_shop():
    res = {}
    with open("jsons/food_services.json", encoding="UTF-8") as food:
        data = json.load(food)
        for el in data:
            res.setdefault(el["TypeObject"], []).append((el["Name"],el["SeatsCount"]))
        for k,v in sorted({k: max(v,key=lambda x: x[1]) for k,v in res.items()}.items()):
            print(f"{k}: {v[0]},{v[1]}")










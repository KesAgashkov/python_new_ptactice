import csv
from datetime import datetime
#1
def exs_1():
    with open('grades.csv', encoding='utf-8') as csv_file:
        # создаем reader объект и указываем в качестве разделителя символ ;
        rows = csv.reader(csv_file, delimiter=';')
        # выводим каждую строку
        for row in rows:
            print(row)

#2
def exs_2():
    with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
        # создаем writer объект и указываем названия столбцов
        writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
        # записываем первую строку с названиями столбцов
        writer.writeheader()
        # записываем строку с данными
        writer.writerow({'first_col': 'value1', 'second_col': 'value2'})

#3
def exs_3():
    with open('csv/sales.csv', encoding='utf-8') as file:
        data = file.read()
        goods = [r.split(';') for r in data.splitlines()]
        del goods[0]
        for el in filter(lambda item: (int(item[1])-int(item[2])>0), goods):
            print(el[0])

#4
def exs_4():
    with open('csv/salary_data.csv', encoding='utf-8') as file:
        data = file.read()
        companyes= [r.split(';') for r in data.splitlines()]
        del companyes[0]
        dct = {el[0]:[] for el in companyes}
        for el in companyes:
            dct.setdefault(el[0], []).append(int(el[1]))
        dct = {k:sum(v)/len(v) for k,v in dct.items()}
        dct = sorted(dct.items(), key=lambda x: x[1])
        for el in dct:
            print(el[0])

## или вот так
def exs_4_good():
    with open('csv/salary_data.csv', encoding='utf-8') as file:
        d = {}
        for k, v in list(__import__('csv').reader(file, delimiter=';'))[1:]:
            d.setdefault(k, []).append(int(v))
        for k in sorted(d, key=lambda x: (sum(d[x]) / len(d[x]), x)):
            print(k)

#5
def exs_5():
    with open('csv/deniro.csv', encoding='utf-8') as file:
        data = [r for r in csv.reader(file, delimiter=',')]
        sor = 2
        if sor == 1:
            for el in sorted(data):
                print(*el, sep=",")
        else:
            for el in sorted(data, key=lambda x: (int(x[sor-1]),x[0])):
                print(*el, sep=",")
#или вот так
def exs_5_good():
    n = int(input())
    with open(r"csv/deniro.csv", encoding='utf-8') as file:
        rows = csv.reader(file, quotechar='"')
        lst = [(a, int(b), int(c)) for a, b, c in rows]
        for el in sorted(lst, key=lambda x: x[n - 1]):
            print(*el, sep=',')

#6
def exs_6(filename):
    with open(filename, encoding='utf-8') as file:
        res = {}
        for el in csv.DictReader(file):
            for k,v in el.items():
                res.setdefault(k, []).append(v)
    return res
# print(exs("test.csv"))

#7
def diff_task():
    res = {}
    with open("csv/data.csv", encoding='utf-8') as file_in, open("csv/domain_usage.csv", "w", encoding="utf-8", newline='') as file_out:
        data = [el for el in csv.reader(file_in)]
        for el in data[1:]:
            res.setdefault(el[2].split("@")[1], []).append(el[1])
        writer = csv.writer(file_out)
        writer.writerow(("domain","count"))
        for k,v in sorted(res.items(),key=lambda x: (len(x[1]),x[0])):
            writer.writerow((k, len(v)))
# diff_task()

#8
def diff_task_2():
    res = {}
    with open("csv/wifi.csv", encoding='utf-8') as file_in:
        data = [el for el in csv.reader(file_in, delimiter=';')]
        for el in data[1:]:
            res.setdefault(el[1], []).append(int(el[-1]))
        for k, v in sorted(res.items(), key=lambda x: (-sum(x[1]),x[0])):
            print(f"{k}: {sum(v)}")

#9
def survive_on_titanic():
    res_mail = []
    res_wom =[]
    with open("csv/titanic.csv", encoding='utf-8') as file_in:
        data = [el for el in csv.reader(file_in, delimiter=';')]
        print(data)
        for el in data[1:]:
            if el[0] == "1" and float(el[-1])<18:
                if el[2] == "male":
                    res_mail.append(el[1])
                else:
                    res_wom.append(el[1])
    print(*res_mail, sep="\n")
    print(*res_wom, sep="\n")

#10
def hell_task():
    headers = []
    dct = {}
    with open("csv/name_log.csv", encoding='utf-8', ) as file_in:
        data = [el for el in csv.reader(file_in)]
        headers.extend(data.pop(0))
        for el in data:
            tmp_time = datetime.strptime(el[2], '%d/%m/%Y %H:%M')
            dct.setdefault(el[1], []).append((el[0], tmp_time))
    with open("csv/new_name_log.csv", "w", encoding='utf-8', newline='') as file_out:
        writer = csv.writer(file_out, delimiter= "," )
        writer.writerow(headers)
        for k,v in sorted(dct.items(), key=lambda x: x[0]):
            tmp = max(v, key=lambda x:x[1])
            tmp = f"{tmp[0]}", f"{k}", f"{tmp[1].strftime('%d/%m/%Y %H:%M')}"
            writer.writerow(tmp)

#11 spicy
text = '''01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29
03,Artist,David Allan Coe
03,Title,Willie Waylon And Me
03,Time,3:26'''

with open('csv/data.csv', 'w', encoding='utf-8') as file:
    file.write(text)
def condense_csv(filename, id_name):
    res={}
    with open(filename, encoding='utf-8', ) as file_in:
        data = [el for el in csv.reader(file_in)]

        for el in data:
            res.setdefault(el[0], []).append((el[1],el[2]))
        else:
            t = el[0]
        headers = [id_name]
        for el in res[t]:
            headers.append(el[0])

    with open("csv/condensed.csv", "w", encoding='utf-8', newline='') as file_out:
        writer = csv.writer(file_out, delimiter=",")
        writer.writerow(headers)
        tmp = []
        for k, v in res.items():
            tmp.append(k)
            for i in range(len(headers)-1):
                tmp.append(v[i][1])
            writer.writerow(tmp)
            tmp = []

# condense_csv('data.csv', id_name='Position')

#12 spicy
def sort_list_pupils():
    res={}
    with open("csv/student_counts.csv", encoding='utf-8', ) as file_in:
        data = [el for el in csv.reader(file_in)]
        for i in range(1,len(data)):
            for j in range(len(data[0])):
                res.setdefault(data[0][j], []).append((data[i][j]))
        begin = {"year":res.pop("year")}
        key = sorted(res, key = lambda x: (int(x.split("-")[0]),x.split("-")[1]))
        res.update(begin)
        key.insert(0, "year")
        print(res)
    with open("csv/sorted_student_counts.csv", "w", encoding='utf-8', newline='') as file_out:
        writer = csv.writer(file_out, delimiter=",")
        writer.writerow(key)
        for i in range(len(res["year"])):
            tmp = []
            for k in key:
                tmp.append(res[k][i])
            print(tmp)
            writer.writerow(tmp)

#13 spicy
def get_chipiest_good():
    res={}
    with open("csv/prices.csv", encoding='utf-8', ) as file_in:
        data = [el for el in csv.reader(file_in, delimiter=";")]
        head = data.pop(0)
        for el in data:
            for i in range(1,len(data)-1):
                res.setdefault(el[0], []).append((head[i], int(el[i])))
        res = {k: min(v, key=lambda x: x[1])for k,v in res.items()}
        print(f"{min(res.items(), key=lambda x: (x[1][1],x[1]))[1][0]}: {min(res.items(), key=lambda x: (x[1][1],x[1]))[0]}")

















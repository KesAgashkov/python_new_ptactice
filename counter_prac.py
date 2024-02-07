from collections import Counter
from collections import defaultdict
import json
#1
def fir():
    files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
             'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
             'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
             'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
             'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
             'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
             'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
             'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
             'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
             'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
             'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
             'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
             'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']

    c = Counter([el.split(".")[-1] for el in files])
    for k,v in sorted(dict(c).items()):
        print(f"{k}: {v}")

#2
def count_occurences(word, words):
    return Counter(words.lower().split())[word.lower()]


# word = 'Se'
# words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'
#
# print(count_occurences(word, words))

#3
def three():
    for k,v in sorted(Counter(input().split(",")).items()):
        print(f"{k}: {v}")

# или так

# [print(f'{k}: {v}') for k, v in sorted(__import__('collections').Counter(input().split(',')).items())]

#4
def new_task():
    st = "рубашка,футболка,футболка,брюки,футболка,сырный соус,рубашка,носки,рубашка"
    from collections import Counter
    c = Counter(st.split(","))
    shif = len(max(c, key=len))
    for k,v in sorted(c.items()):
        tmp_sum = sum(ord(el) for el in k)
        if " " in list(k):
            tmp_sum -= 32
        print(f"{k.ljust(shif)}: {tmp_sum} UC x {v} = {tmp_sum*v} UC")

#5
def simple_dimple():
    with open("txts/pythonzen.txt", encoding="UTF-8") as file:
         for k,v in sorted(Counter(el.strip().lower() for el in file.read() if el.isalpha()).items()):
             print(f"{k}: {v}")

#6
def search_most_common():
    print(max(Counter(input().lower().split()).items(), key=lambda x: x[1])[0])

#7
def search_min_common():
    c = Counter(input().lower().split())
    mi = c.most_common()[-1][1]
    print(*sorted([k for k,v in c.items() if v == mi]), sep = ", ")

#8
def search_max_el():
    c = Counter(input().lower().split())
    ma = c.most_common()[0][1]
    print(max([k for k,v in c.items() if v == ma]))

#9
def search_len_words():
    c = Counter([len(el) for el in input().split()])
    for k, v in sorted(c.items(), key=lambda x: x[1]):
        print(f"Слов длины {k}: {v}")

#10
def sear_prelow_pupil():
    lst = sorted([(el.strip().split()[0], int(el.strip().split()[1])) for el in sys.stdin], key=lambda x: x[1])
    print(lst[1][0])

#11
def use_add_attr():
    data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
    data.max_values = lambda: [(k,v) for k,v in data.items() if v == max(data.values())]
    data.min_values = lambda: [(k,v) for k,v in data.items() if v == min(data.values())]

#12
import csv
def csv_to_counter():
    with open("csv/name_log (1).csv", encoding="utf-8") as file:
       for k,v in sorted(Counter([el[1] for el in csv.reader(file)][1:]).items()):
           print(f"{k}: {v}")

#13
def scrabble(symbols, word):
    return Counter(symbols.lower())>=(Counter(word.lower()))

# print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))

#14
def print_bar_chart(data, mark):
    c = Counter(data)
    align = len(max(data, key=len))
    for k,v in sorted(c.items(), key=lambda x:-x[1]):
        print(f"{k.ljust(align)} |{v*mark}")

# print_bar_chart(['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java'], '+')

#15
def find_total():
    prelst = []
    dct = {}
    total = 0
    for i in range(1,5):
        with open(f"quarter{i}.csv", encoding="utf-8") as file:
            prelst.extend([el for el in csv.reader(file)][1:])
    for el in prelst:
        dct.setdefault(el[0], []).append(sum(list(map(int, el[1:]))))
    with open("jsons/prices.json", encoding="utf-8") as j:
        dct_price = json.load(j)
    for el in dct:
        total += sum(dct[el]) * dct_price[el]
    return total

#16
def diff_task():
    total = 0
    c = Counter(map(int,input().split()))
    for i in range(int(input())):
        cl, price = list(map(int,input().split()))
        if cl in c.keys() and c[cl] != 0:
            total+=price
            c[cl] -= 1
    print(total)

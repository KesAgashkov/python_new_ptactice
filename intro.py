##1
def hide_card(card):
    return "*"*12 + card.replace(" ", "")[12:]

##2
def same_parity(sp):
    if not sp:
        return []
    n = sp[0]%2
    if not n:
        return [el for el in sp if el%2 == 0]
    else:
        return [el for el in sp if el%2 == 1]

 ## или вот так
def same_parity(nums):
    return [i for i in nums if i % 2 == nums[0] % 2]

##3

def is_valid(pin):
    return (not(pin.isspace()) and len(pin) in (4,5,6) and pin.isdigit())

##4

def print_given(*args, **kwargs):
    for el in args:
        print(el, type(el))
    for k,v in sorted(kwargs.items()):
        print(k, v, type(v))

# print_given(b=2, d=4, c=3, a=1)

##5

def convert(st):
    low = 0
    up = 0
    for el in st:
        if el.isalpha():
            if el.islower():
                low+=1
            else:
                up+=1
    return st.lower() if low>=up else st.upper()

# print(convert("pi31415!"))

##5

def filter_anagrams(word, words):
    w = sorted(list(word))
    res= []
    for el in words:
        c = sorted(list(el))
        print(c)
        if c == w:
            res.append(el)
    print(el)

# или так
def filter_anagrams(word, anagrams):
    return [anagram for anagram in anagrams if sorted(anagram) == sorted(word)]

##6

def likes(names):
    if not names:
        return "Никто не оценил данную запись"
    elif len(names) == 1:
        return f"{names[0]} оценил(а) данную запись"
    elif len(names) == 2:
        return f"{names[0]} и {names[1]} оценили данную запись"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
    else:
        return f"{names[0]}, {names[1]} и {len(names)-2} других оценили данную запись"

##7

def index_of_nearest(numbers, number):
    if not numbers:
        return -1
    min =abs(numbers[0] - number)
    for el in numbers:
        if abs(el - number) < min:
            min = el - number
    return numbers.index(min+number)

# print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0))

##8

def spell (*args):
    emp_dict = {el[0]: [] for el in args}
    for el in args:
        emp_dict[el[0]].append(len(el))
    return {k: max(v) for k, v in emp_dict.items()}


# или так

def spell(*args):
    return {i[0].lower():len(i) for i in sorted(args, key=len)}

# words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
# print(spell(*words))

##9
def choose_plural(amount, declensions):
    if str(amount)[-1] == "1" and str(amount)[-2:] != "11":
        return f"{amount} {declensions[0]}"
    elif str(amount)[-1] in ("2", "3", "4") and str(amount)[-2:] not in ("11", "12", "13", "14"):
        return f"{amount} {declensions[1]}"
    else:
        return f"{amount} {declensions[2]}"

# print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))

##10

def get_biggest(numbers):
    if not numbers:
        return -1
    return int(''.join(sorted(map(str, numbers), key=lambda x: x*len(max(map(str, numbers), key=len)), reverse=True)))

# print(get_biggest( [6, 65, 345, 3, 487, 40]))

#11

def dist (d1,d2,d3):
    fir =  min(d1, (d2+d3))
    sec = min(d3, (d1 + d2))
    th = min(d2, (d3 + d1))
    return fir+sec+th

# print(dist(10,20,30))

#12
def func():
    n = 9
    lst = [i for i in range(1,n+1)]
    x,y,a,b = 3,6,5,8
    if x == 1:
        lst_1 = []
    else:
        lst_1 = lst[:x-1]
    lst_2 = lst[x-1:y][::-1]
    if y>=n:
        lst_3 = []
    else:
        lst_3 = lst[y:]
    prelist = lst_1+lst_2+lst_3

    if a == 1:
        pre_1 = []
    else:
        pre_1 = prelist[:a-1]
    pre_2 = prelist[a-1:b][::-1]
    if b>=n:
        pre_3 = []
    else:
        pre_3 = prelist[b:]

    res = pre_1+pre_2+pre_3
    return res

#13

def another():
    nums = list(map(int, input().split()))
    res = []
    count = 1
    for i in range (len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i!=j:
                res.append(nums[i])
                break
    print(*sorted(set(res)))

#14

def group_numbers():
    dct = {}
    for el in range(1, int(input()) + 1):
        summa = sum(map(int, str(el)))
        dct.setdefault(summa, []).append(el)
    print(len(max(dct.values(), key=len)))

#15

def lang__for_film():
    n = int(input())
    res = []
    for i in range(n):
        res.append(set(input().split(", ")))
    for i in range(1, len(res)):
        res[0] = res[0].intersection(res[i])

    print(*sorted(res[0]), sep=", ") if res[0] else print("Сериал снять не удастся")

#16

def similar_words():
    # Решай через определение индексов гласных букв
    base = list(input())
    n = int(input())
    examples = [input() for i in range(n)]
    glas = "а, у, о, ы, и, э, я, ю, ё, е".split(", ")
    sample = []
    compare = []
    tmp = []
    res_list = []
    count_gl = 0
    for el in base:
        if el in glas:
            sample.append(base.index(el))
            base[base.index(el)] = 0
    for el in examples:
        tmp = list(el)
        print(tmp)
        for ch in el:
            if ch in glas:
                compare.append(tmp.index(ch))
                tmp[tmp.index(ch)] = 0
        if compare == sample:
            res_list.append(el)
        compare = []
    print(*res_list, sep="\n")

# similar_words()

#17

def scary_task_mail ():
    mail = ["ivan-petrov@beegeek.bzz", "petr-ivanov@beegeek.bzz", "ivan-petrov1@beegeek.bzz", "ivan-ivanov@beegeek.bzz",
            "ivan-ivanov1@beegeek.bzz", "ivan-ivanov2@beegeek.bzz"]
    name = ["ivan-ivanov",  "petr-petrov", "petr-ivanov"]
    res = []
    last = mail[0][mail[0].index("@"):]
    prom_lst = []
    nums_mail = []
    for el in name:
        if el not in "".join(mail):
            tmp = el + last
            res.append(tmp)
            mail.append(tmp)
        else:
            prom_lst = [e for e in mail if el in e]
            nums_mail = [e[len(el):e.index("@")] for e in prom_lst]
            if "" not in nums_mail:
                tmp = el + last
                res.append(tmp)
                mail.append(tmp)
            else:
                for i in range(1, 15):
                    if str(i) not in nums_mail:
                        tmp = el + str(i) + last
                        res.append(tmp)
                        mail.append(tmp)
                        break
                    else:
                        continue
        print(res)

#18

def hellish_task():
    data =[]
    with open("txts/files.txt", "r", encoding="UTF-8") as f:
        for line in f:
            line = line.rstrip("\n")
            data.append(line)

    dct = {el[el.index(".")+1:el.index(" ")]: [] for el in data}

    for el in data:
        tmp = el[el.index(".")+1:el.index(" ")]
        dct.setdefault(tmp, []).append(el)

    for k,v in sorted(dct.items()):
        sigh = "B"
        summ = 0
        for el in sorted(v):

            ed = el[el.rfind(" ")+1:]
            zn = int(el[el.find(" "):el.rfind(" ")])
            print(el[:el.find(" ")])
            if ed == "B":
                summ += zn
            elif ed == "KB":
                summ += zn * 1024
            elif ed == "MB":
                summ += zn * 1024*1024
            else:
                summ += zn * 1024 * 1024 * 1024

        if (1024*1024) > summ> 1024:
            sign = "KB"
            res = str(round(int(summ)/1024)).rstrip(".0")
            summ = f"{res} {sign}"
        elif (1024*1024*1024) > summ > (1024*1024):
            sign = "MB"
            res = str(round(int(summ) / (1024*1024)))
            summ = f"{res} {sign}"
        else:
            sign = "GB"
            res = str(round(int(summ) / (1024 * 1024 * 1024)))
            summ = f"{res} {sign}"
        print("----------")
        print(f"Summary: {summ}")
        print()


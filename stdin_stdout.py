import email.header
import sys
import datetime

# for line in sys.stdin:
#     print(line.strip('\n'))


#1
def fir():
    print(*["".join(list(el)[::-1]) for el in [line.strip() for line in sys.stdin]], sep="\n")
    #или так
    [print(e.strip()[::-1]) for e in sys.stdin]
#2
def sec():
    lst = [datetime.datetime.fromisoformat(e.strip()) for e in sys.stdin]
    print((max(lst)-min(lst)).days)
#3
def winner_socks():
    import sys
    lst = [int(e.strip()) for e in sys.stdin]
    mark = len(lst) % 2
    if mark == 0:
        print("Дима" if lst[-1] % 2 == 0 else "Анри")
    else:
        print("Анри" if lst[-1] % 2 == 0 else "Дима")
#4
def hights_pupils():
    lst = [int(e.strip()) for e in sys.stdin]
    if lst:
        print(f"Рост самого низкого ученика: {min(lst)}", f"Рост самого высокого ученика: {max(lst)}",
              f"Средний рост: {sum(lst) / len(lst)}", sep="\n")
    else:
        print("нет учеников")
#5
def get_count_comment():
    print(len([e.strip() for e in sys.stdin if "#" == list(e.strip())[0]]))
#6
import sys
def del_comment_from_code():
    print(*[e for e in sys.stdin if "#" != list((e+"1").strip())[0]] ,sep="")
#7
def get_aprove_news():
    prelst = [e for e in sys.stdin]
    rub = prelst.pop(-1).strip()
    news = {e.strip().split(" / ")[1]: [] for e in prelst}
    for el in prelst:
        news.setdefault(el.strip().split(" / ")[1], []).append((float(el.strip().split(" / ")[2]), el.strip().split(" / ")[0]))
    print( *[el[1] for el in sorted(news[rub])], sep="\n")

#8
import datetime
def new_task():

    prelst = [datetime.date(int(e.split(".")[2]),int(e.split(".")[1]),int(e.split(".")[0])) for e in sys.stdin]
    top, low = 0, 0
    for i in range(len(prelst)-1):
        if prelst[i]<prelst[i+1]:
            top+=1
        elif prelst[i]>prelst[i+1]:
            low+=1
    if top+1 == len(prelst):
        res = "ASC"
    elif low+1 == len(prelst):
        res = "DESC"
    else:
        res = "MIX"
    print(res)

#9
def define_progression():
    lst = [int(e.strip()) for e in sys.stdin]
    step_ar = lst[1]-lst[0]
    step_geo = lst[1]/lst[0]
    ar, geom = True, True
    tot_geom = 0
    for i in range(len(lst)-1):
        tot_geom = lst[i]*step_geo
        if lst[i+1] != lst[i]+step_ar:
            ar = False
        if lst[i+1] != tot_geom:
            geom = False
    if not ar and not geom:
        print("Не прогрессия")
    else:
        print("Арифметическая прогрессия" if ar else "Геометрическая прогрессия")



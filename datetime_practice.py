import sys
from datetime import date,time

#1
def get_min_max(dates):
    if not dates:
        return ()
    else:
        return (min(dates), max(dates))

#2
def get_date_range(date1,date2):
    res = []
    if date1>date2:
        return []
    else:
        date1 = date1.toordinal()
        date2 = date2.toordinal()
    while date1<=date2:
        res.append(date.fromordinal(date1))
        date1+=1
    return res

#3

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

def saturdays_between_two_dates(date1,date2):
    minn = min(date1,date2)
    maxx = max(date1,date2)
    count = 0
    if date1 == date2 and date1.isoweekday() == 6:
        return 1
    elif date1 == date2:
        return 0
    else:
        minn = minn.toordinal()
        maxx = maxx.toordinal()
        while minn<=maxx:
            if date.fromordinal(minn).isoweekday() == 6:
                count += 1
            minn += 1
    return count

# print(saturdays_between_two_dates(date1, date2))

#3
def form():
    alarm = time(7, 30, 25)
    print('Часы:', alarm.strftime('%H'))
    print('Минуты:', alarm.strftime('%M'))
    print('Секунды:', alarm.strftime('%S'))


    birthday = date(1992, 10, 6)
    print('Название месяца:', birthday.strftime('%B'))
    print('Название дня недели:', birthday.strftime('%A'))
    print('Год:', birthday.strftime('%Y'))
    print('Месяц:', birthday.strftime('%m'))
    print('День:', birthday.strftime('%d'))

#4
def more_ex():
    from datetime import date
    print(min(date.fromisoformat(input()), date.fromisoformat(input())).strftime('%d-%m (%Y)'))

#5
def diff_task():
    from datetime import date
    dates = [date.fromisoformat(input()) for i in range(int(input()))]
    dates = sorted(dates)
    for el in dates:
        day = "0"+str(el.day) if len(str(el.day))==1 else str(el.day)
        mo = "0"+str(el.month) if len(str(el.month))==1 else el.month
        yar = str(el.year).lstrip("0")
        print(f"{day}/{mo}/{yar}")

#6

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
def print_good_dates(dates):
    yr = 1992
    age = 29
    for el in sorted(dates):
        if el.year == yr and (el.day+el.month) == age:
            print(el.strftime("%B %d, %Y"))

# print_good_dates(dates)

#7

def is_correct(day, month, year):
    try:
        j = date.fromisoformat(f"{year}-{month}-{day}")
        return True
    except ValueError:
        return False

# print(is_correct(28,12,2021))

#8

def correct_dates():
    from datetime import date
    count = 0
    while True:
        el = input()
        if el == "end": break
        el = el.split(".")
        try:
            d = date.fromisoformat(f"{el[2]}-{el[1]}-{el[0]}")
            print("Корректная")
            count += 1
        except ValueError:
            print("Некорректная")
    print(count)

#тип данных datetime

from datetime import datetime, date, time
#9
def parse_txt_to_datetime():
    text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
    dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
    print(dt)

#10
def sec_datetime_and_back():
    seconds = 2483228800
    dt = datetime(2011, 11, 4)
    print(datetime.fromtimestamp(seconds))
    print(dt.timestamp())

#11
def simple_task():
    times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
                          datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
                          datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
                          datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
                          datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
                          datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
                          datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
                          datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
                          datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
                          datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
                          datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
                          datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
                          datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
                          datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

    before = [el for el in times_of_purchases if el.hour < 12]
    print("До полудня" if len(before) > (len(times_of_purchases) - len(before)) else "После полудня")

#12
def more_task():
    dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
             date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
             date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

    times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
             time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
             time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

    print(*sorted([datetime.combine(dat, tim) for dat,tim in zip(dates,times)], key = lambda x: x.second), sep="\n")

#13
def serch_min_res():
    data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
            'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
            'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
            'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
            'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
            'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
            'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
            'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
            'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
            'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
            'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}


    new = {k:datetime.strptime(v[1],'%d.%m.%Y %H:%M:%S') - datetime.strptime(v[0],'%d.%m.%Y %H:%M:%S') for k,v in data.items()}
    print(min(new.items(), key=lambda item: item[1])[0])

#14
def gruming_astro_diary():
    data = []
    tmp = ""
    with open("diary.txt", "r", encoding="UTF-8") as f:
        for line in f:
            tmp+=line
    data = tmp.split("\n\n")
    dct = {}
    for el in data:
        dct[datetime.strptime(el.split("\n")[0],"%d.%m.%Y; %H:%M")] = el
    for k,v in sorted(dct.items()):
        print(v)
        print()

#15

dates = ['01.11.2021', '05.11.2021']
some_date = '01.11.2021'

def is_available_date(dates, some_date):
    cash_reserv = []
    booking_dates = []
    flag = True
    for el in dates:
        if len(el)<11:
            tmp = datetime.strptime(el,'%d.%m.%Y')
            tmp = tmp.toordinal()
            cash_reserv.append(tmp)
        else:
            st, fin = datetime.strptime(el.split("-")[0],'%d.%m.%Y'), datetime.strptime(el.split("-")[1],'%d.%m.%Y')
            st, fin = st.toordinal(), fin.toordinal()
            cash_reserv.extend([i for i in range (st,fin+1)])
            print(cash_reserv)
    if len(some_date)<11:
        tmp = datetime.strptime(some_date, '%d.%m.%Y')
        tmp = tmp.toordinal()
        booking_dates.append(tmp)
        print(booking_dates)
    else:
        st, fin = datetime.strptime(some_date.split("-")[0], '%d.%m.%Y'), datetime.strptime(some_date.split("-")[1], '%d.%m.%Y')
        st, fin = st.toordinal(), fin.toordinal()
        booking_dates.extend([i for i in range(st, fin + 1)])
        print(booking_dates)

    for el in booking_dates:
        if el in cash_reserv:
            flag = False
            break
    return flag

# print(is_available_date(dates, some_date))

#тип данных timedelta

#16
from datetime import datetime, timedelta,date
def use_delta():
    dt = datetime(2021, 11, 4, 13, 6) + timedelta(hours=12, weeks = 1)
    print(dt.strftime('%d.%m.%Y %H:%M:%S'))

#17
def onemore():
    today = date(2021, 11, 4)
    birthday = date(2022, 10, 6)
    days = birthday - today
    print(days.days)

#18
def more_ex():
    from datetime import timedelta, date, datetime
    dt = datetime.strptime(input(), '%d.%m.%Y')
    print((dt - timedelta(days=1)).strftime('%d.%m.%Y'))
    print((dt + timedelta(days=1)).strftime('%d.%m.%Y'))

#19
def simple():
    dt = datetime.strptime(input(), '%H:%M:%S')
    print(dt.hour*3600 + dt.minute*60 + dt.second)

#20
def more_diff():
    dt = datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=int(input()))
    print(dt.strftime('%H:%M:%S'))

#21
year = 2022
def num_of_sundays(year):
    start = datetime(year, 1, 1)
    count=0
    while start.year == year:
        if start.strftime("%w")=="0":
            count+=1
        start = start + timedelta(days=1)
    return count

# print(num_of_sundays(year))

# или так
def num_of_sundays(year):
    return date(year, 12, 31).strftime('%U')

#22
def new_task():
    dt = datetime.strptime(input(), '%d.%m.%Y')
    print(dt.strftime('%d.%m.%Y'))
    for i in range(2,11):
        dt += timedelta(days=i)
        print(dt.strftime('%d.%m.%Y'))

#23
import sys
def again_task(dat):
    res = []
    dates = [datetime.strptime(el,'%d.%m.%Y') for el in dat.split(" ")]
    if len(dates) == 1 or not dates:
        print(res)
        sys.exit()
    else:
        for i in range(len(dates)-1):
            res.append(abs(dates[i]-dates[i+1]).days)
    print( res)

#24
dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
def fill_up_missing_dates(dates):
    res = []
    dates = sorted([datetime.strptime(el, '%d.%m.%Y') for el in dates])
    res.append(dates[0].strftime('%d.%m.%Y'))
    tmp = dates[0]
    while True:
        tmp += timedelta(days=1)
        if tmp > max(dates):
            break
        if tmp not in dates:
            res.append(tmp.strftime('%d.%m.%Y'))
        else:
            res.append(tmp.strftime('%d.%m.%Y'))
    print(res)

# fill_up_missing_dates(dates)

#25
from datetime import datetime, timedelta,date
def create_chedule():
    start = datetime.strptime("10:00", '%H:%M')
    stop = datetime.strptime("12:35", '%H:%M')
    tmp = start
    while True:
        if tmp+timedelta(minutes=45) > stop:
            break
        print(f"{tmp.strftime('%H:%M')} - {(tmp + timedelta(minutes=45)).strftime('%H:%M')}")
        tmp += timedelta(minutes=55)

#26
def search_diff():
    data = [('07:14', '08:46'),
            ('09:01', '09:37'),
            ('10:00', '11:43'),
            ('12:13', '13:49'),
            ('15:00', '15:19'),
            ('15:58', '17:24'),
            ('17:57', '19:21'),
            ('19:30', '19:59')]
    summ = 0
    for el in data:
        summ += (datetime.strptime(el[1], '%H:%M') - datetime.strptime(el[0], '%H:%M')).total_seconds()/60
    print(int(summ))

#27
def count_weekdays():
    start, stop = "13.01.0001", "13.12.9999"
    pn,vt,sr,cht,pt,sb,vs = 0,0,0,0,0,0,0
    nach, oko= datetime.strptime(start, '%d.%m.%Y').year, datetime.strptime(stop, '%d.%m.%Y').year
    for i in range(nach, oko+1):
        start = datetime.strptime(f"13.01.{str(i).zfill(4)}", '%d.%m.%Y')
        for j in range(1,13):
            start = datetime.strptime(f"13.{str(j).zfill(2)}.{str(i).zfill(4)}", '%d.%m.%Y')
            if start.isoweekday() == 1:
                pn+=1
            elif start.isoweekday() == 2:
                vt+=1
            elif start.isoweekday() == 3:
                sr+=1
            elif start.isoweekday() == 4:
                cht+=1
            elif start.isoweekday()== 5:
                pt+=1
            elif start.isoweekday() == 6:
                sb+=1
            elif start.isoweekday() == 7:
                vs+=1

    print(pn,vt,sr,cht,pt,sb,vs, sep="\n")

#28
def  schedule_shop():
    t = datetime.strptime(input(), '%d.%m.%Y %H:%M')
    schedule = {
        1: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
        2: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
        3: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
        4: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
        5: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
        6: {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
        7: {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
        }

    if schedule[t.isoweekday()]["start"].seconds/3600<=t.hour<schedule[t.isoweekday()]["end"].seconds/3600:
        print(int(schedule[t.isoweekday()]["end"].seconds/60 - (t.hour*60 + t.minute)))
    else:
        print("Магазин не работает")

#29
def diff_condition():
    start,stop = datetime.strptime("30.04.2021", '%d.%m.%Y'), datetime.strptime("10.05.2021", '%d.%m.%Y')
    while (start.day+start.month)%2 == 0:
        start+=timedelta(days=1)
    while start <= stop:
        if start.isoweekday() not in (1,4):
            print(start.strftime('%d.%m.%Y'))
        start += timedelta(days=3)

#30
def search_oldest_pers():
    stuff = [input() for i in range(int(input()))]
    stuff_res = {datetime.strptime(el.split(" ")[-1], '%d.%m.%Y'):  [] for el in stuff}
    for el in stuff:
        stuff_res.setdefault(datetime.strptime(el.split(" ")[-1], '%d.%m.%Y'),[]).append(el.split()[:2])
    if len(stuff_res[min(stuff_res)]) == 1:
        print(min(stuff_res).strftime('%d.%m.%Y'), *stuff_res[min(stuff_res)][0])
    else:
        print(min(stuff_res).strftime('%d.%m.%Y'), len(stuff_res[min(stuff_res)]))

#31
def search_similar_bdate():
    stuff = [input() for i in range(int(input()))]
    stuff_res = {datetime.strptime(el.split(" ")[-1], '%d.%m.%Y'):  [] for el in stuff}
    for el in stuff:
        stuff_res.setdefault(datetime.strptime(el.split(" ")[-1], '%d.%m.%Y'),[]).append(el.split(" ")[-1])

    prom = [len(stuff_res[el]) for el in stuff_res]
    for el in sorted(stuff_res):
        if len(stuff_res[el]) == max(prom):
            print(el.strftime('%d.%m.%Y'))

from datetime import datetime, timedelta,date

#32
def get_bdays():
    res = {}
    check_sta = datetime.strptime(input(), '%d.%m.%Y')
    check_stop = check_sta + timedelta(days=7)
    stuff = [input() for i in range(int(input()))]
    stuff_res = {datetime.strptime(el.split(" ")[-1], '%d.%m.%Y'): " ".join(el.split(" ")[:2]) for el in stuff}
    for k, v in stuff_res.items():
        tmp = k
        if check_sta < tmp.replace(year=check_sta.year) <= check_stop \
                or check_sta < tmp.replace(year=check_sta.year + 1) <= check_stop:
            res[k] = v
    if res:
        print(res[max(res)])
    else:
        print("Дни рождения не планируются")


import sys

#32
def final_task():
    check = datetime.strptime("08.11.2022 ровно в 12:00", '%d.%m.%Y  ровно в %H:%M')
    dat = datetime.strptime("08.11.2022 11:58", '%d.%m.%Y %H:%M')
    if check<=dat:
        print("Курс уже вышел!")
    else:
        diff = check - dat
        diff1 = str(diff)
        print(diff1)
        tmp = ""
        if "day" in diff1:
            if diff1.split(" ")[0][-1] == "1" and diff1.split(" ")[0] != "11":
                tmp += diff1.split(" ")[0] + " день "
            elif diff1.split(" ")[0] == "8212":
                tmp += diff1.split(" ")[0] + " дней "
            elif diff1.split(" ")[0][-1] in ("2", "3", "4") and diff1.split(" ")[0] not in ("11", "12", "13", "14"):
                tmp += diff1.split(" ")[0] + " дня "
            else:
                tmp += diff1.split(" ")[0] + " дней "
            if diff1.split(" ")[2][0] != "0":
                hour = diff1.split(" ")[2].split(":")[0]
                if hour[-1] == "1" and hour != "11":
                    tmp +="и " + hour + " час "
                elif hour[-1] in ("2", "3", "4") and hour not in ("11", "12", "13", "14"):
                    tmp += "и " + hour + " часа "
                else:
                    tmp += "и " + hour + " часов "
        else:
            if diff1.split(":")[0][0] != "0":
                hour = diff1.split(":")[0]
                if hour[-1] == "1" and hour != "11":
                    tmp += "и " + hour + " час "
                elif hour[-1] in ("2", "3", "4") and hour not in ("11", "12", "13", "14"):
                    tmp += hour + " часа "
                else:
                    tmp += hour + " часов "
                if diff1.split(":")[1] != "00":
                    minute = diff1.split(":")[1]
                    if minute[-1] == "1" and minute != "11":
                        tmp += "и " + minute + " минута"
                    elif minute[-1] in ("2", "3", "4") and minute not in ("11", "12", "13", "14"):
                        tmp += "и " + minute + " минуты"
                    else:
                        tmp += "и " + minute + " минут"
            else:
                minute = diff1.split(":")[1]
                if minute[-1] == "1" and minute != "11":
                    tmp += minute + " минута"
                elif minute[-1] in ("2", "3", "4") and minute not in ("11", "12", "13", "14"):
                    tmp += str(int(minute)) + " минуты"
                    print(tmp)
                else:
                    tmp += minute + " минут"

print(f"До выхода курса осталось: {tmp.strip()}")


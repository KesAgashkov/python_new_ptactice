import calendar, locale, datetime
from datetime import timedelta
# print(calendar.calendar(2021))
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# print(calendar.calendar(2021))
#1
def fir():
    print(*[calendar.isleap(int(input())) for i in range(int(input()))], sep="\n")
#2
def sec():
    ya, mo = input().split(" ")
    print(calendar.month(int(ya), list(calendar.month_abbr).index(mo)))
#3
def th():
    ya,mo,da = map(int, input().split("-"))
    print(list(calendar.day_name)[calendar.weekday(ya, mo, da)])
#4
def four():
    ya, mo = map(int, input().split(" "))
    print(calendar.monthrange(ya, mo)[1])
#5
def five():
    ya,mo = input().split(" ")
    mo = list(calendar.month_name).index(mo)
    print(calendar.monthrange(int(ya), mo)[1])
#6
def get_days_in_month(year):
    res = []
    month = list(calendar.month_name).index(month)
    repeat = calendar.monthrange(year, month)[1]
    for i in range(1, repeat+1):
        res.append(datetime.date(year, month, i))
    return res
#7
def get_all_mondays(year):
    start = datetime.date(int(year),1,1)
    tmp = start
    res = []
    while True:
        if tmp.isoweekday() == 1:
            res.append(tmp)
        tmp += datetime.timedelta(days=1)
        if start.year!=tmp.year:
            break
    return res
# print(get_all_mondays(111))
#8

for i in range(1, 13):
    ya = int(2021)
    tmp_cal = calendar.monthcalendar(ya, i)
    for j in range(len(tmp_cal)):
        if tmp_cal[j][3]!=0:
            print(f"{tmp_cal[2][3]}.{str(i).zfill(2)}.{ya}")
        else:
            print(f"{tmp_cal[3][3]}.{str(i).zfill(2)}.{ya}")
        break



#Could use cleaning up.  I feel like there's amod way to do it without so many nested ifs
import calendar
from datetime import date

week = {}
for j in range(7):
    week[calendar.day_name[j]] = j

def meetup_day(year, month, weekday, cardinal):
    thirteenth_weekday = date(year, month, 13).weekday()
    last_day = calendar.monthrange(year, month)[1]
    last_monday = last_day - date(year, month, last_day).weekday()

    if cardinal == 'teenth':
        if thirteenth_weekday > week[weekday]:
            day = 20 - thirteenth_weekday + week[weekday]
        else:
            day = 13 + (week[weekday] - thirteenth_weekday)
    elif cardinal == 'last':
        if date(year, month, last_day).weekday() >= week[weekday]:
            day = last_monday + week[weekday]
        else:
            day = last_monday - (-week[weekday]%7)

    else:
        for i in range(1,8):
            weekday_num = date(year, month, i).weekday()
            if calendar.day_name[weekday_num] == weekday:
                break
        day = 7 * (int(cardinal[0])-1) + i

    return date(year, month, day)

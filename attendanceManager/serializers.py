from datetime import datetime
from .models import TimeTable, LectureHall


def get_period_cell(lh, _now_time = None):
    period = ""
    days = {
        0: "monday",
        1: "tuesday",
        2: "wednesday",
        3: "thursday",
        4: "friday",
        5: "saturday",
        6: "sunday",
    }

    cell = "1"
    # _time1 = datetime.strptime(, "%H:%M").time()
    if _now_time == None:
        _now_time = datetime.now()
    else:
        print(_now_time)
        _now_time = datetime.strptime(_now_time[:5], "%H:%M").time()
    # _weekday = days[_now_time.weekday()]
    _weekday = 0
    print(_now_time.weekday())

    _lhall = LectureHall.objects.get(className=lh)
    data = TimeTable.objects.filter(Class=_lhall, day=days[_weekday])

    if list(data) != []:
        for i in enumerate(data):
            if i[1].day == days[_weekday] and (
                i[1].start <= _now_time.time() and i[1].end >= _now_time.time()
            ):
                cell = i[0] + 1
                period = i[1].period
                break

    # data.
    # print(data, _lhall)

    # _time2 = datetime.strptime(, "%H:%M").time()
    # print(_time1 < _now_time, _now_time < _time2)

    # DATA
    # 08:30-09:30=DBMS||09:30-10:30=VERBAL||10:50-11:50=DM||11:50-12:50=MPMC||[01:40-02:40,02:40-03:25,03:45-04:30]=MPMC LAB

    return cell, period


def set_cell(period, cell, instance):
    if cell == 1:
        instance[0].h1 = period
    elif cell == 2:
        instance[0].h2 = period
    elif cell == 3:
        instance[0].h3 = period
    elif cell == 4:
        instance[0].h4 = period
    elif cell == 5:
        instance[0].h5 = period
    elif cell == 6:
        instance[0].h6 = period
    elif cell == 7:
        instance[0].h7 = period

    instance[0].save()
    return instance[0]


def get_cell_data(cell, instance):
    if cell == 1:
        if instance.h1 == None:
            return None
        return {
            "present": instance.h1.split(":")[1] == "PRESENT",
            "od": instance.h1.split(":")[1] == "OD",
        }
    elif cell == 2:
        if instance.h2 == None:
            return None
        return {
            "present": instance.h2.split(":")[1] == "PRESENT",
            "od": instance.h2.split(":")[1] == "OD",
        }
    elif cell == 3:
        if instance.h3 == None:
            return None
        return {
            "present": instance.h3.split(":")[1] == "PRESENT",
            "od": instance.h3.split(":")[1] == "OD",
        }
    elif cell == 4:
        if instance.h4 == None:
            return None
        return {
            "present": instance.h4.split(":")[1] == "PRESENT",
            "od": instance.h4.split(":")[1] == "OD",
        }
    elif cell == 5:
        if instance.h5 == None:
            return None
        return {
            "present": instance.h5.split(":")[1] == "PRESENT",
            "od": instance.h5.split(":")[1] == "OD",
        }
    elif cell == 6:
        if instance.h6 == None:
            return None
        return {
            "present": instance.h6.split(":")[1] == "PRESENT",
            "od": instance.h6.split(":")[1] == "OD",
        }
    elif cell == 7:
        if instance.h7 == None:
            return None
        return {
            "present": instance.h7.split(":")[1] == "PRESENT",
            "od": instance.h7.split(":")[1] == "OD",
        }




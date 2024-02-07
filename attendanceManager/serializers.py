from datetime import datetime
from .models import TimeTable, LectureHall, LectureHallAttadence, Student
from lecture_hall.models import Subject

def convert_to_datetime(railway_time):
    normal_time = railway_time.strftime("%I:%M %p")
    return normal_time

def get_period_cell(lh, _now_time=None):
    days = {
        0: "monday",
        1: "tuesday",
        2: "wednesday",
        3: "thursday",
        4: "friday",
        5: "saturday",
        6: "sunday",
    }

    startTime = ""
    endTime = ""
    cell = 7
    period = ""
    if _now_time is not None:
        print("attendanceManager.views stud:", _now_time[:5])
        startTime = _now_time[:5]
        endTime = _now_time[8:]

    _weekday = datetime.now().weekday()

    _lhall = LectureHall.objects.get(className=lh)
    data = TimeTable.objects.filter(
        Class=_lhall,
        day=days[_weekday],
    )
    # print("attendanceManager.serializers TimeTable data", data)

    if list(data) != []:
        for i, e in enumerate(data):
            classPeriod = e.returnData()
            print(
                f"classPeriod.start {str(convert_to_datetime(classPeriod['start']))[:-3]} and classPeriod.end {str(convert_to_datetime(classPeriod['end']))[:-3]}, {startTime}, {endTime}"
            )

            if (
                str(convert_to_datetime(classPeriod["start"]))[:-3] >= startTime
                and str(convert_to_datetime(classPeriod["end"]))[:-3] <= endTime
            ):
                print("classPeriod.hour", classPeriod["hour"])
                cell = int(classPeriod["hour"])
                period = classPeriod["period"]
                break

    return cell, period


def set_cell(period, cell, instance):
    # print("CellsType: ", type(cell))
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


def get_subject_attendance(lh, studentName):
    data = {}

    attendance = {}

    try:
        lh = list(LectureHall.objects.filter(className=lh))
        print(studentName)
        student = Student.objects.get(rollNumber=studentName)
        if list(lh) != []:
            subjects = list(Subject.objects.filter(_lh=lh[0]))
            attendanceObjects = list(
                LectureHallAttadence.objects.filter(Class=lh[0], name=student)
            )
            
            for i in subjects:
                attendance[i.subjectName] = {"total": 0, "presence": 0}

            for i in attendanceObjects:
                periods = i.returnPeriods()
                for j in range(len(periods)):
                    if periods[j + 1] != None:
                        raw_data = str(periods[j + 1]).split(":")
                        print("periods", j, raw_data)
                        attendance[raw_data[0]]["total"] += 1
                        if raw_data[1] == "PRESENT":
                            attendance[raw_data[0]]["presence"] += 1
                    
            print("attendance", attendance)

            for i in attendance:
                if attendance[i]["presence"] == 0 or attendance[i]["total"] == 0:
                    data[i] = 0
                else:
                    data[i] = (attendance[i]["presence"] / attendance[i]["total"]) * 100

        else:
            return
    except Exception as e:
        print("Error in attendanceManager.serializers:", e)

    return data

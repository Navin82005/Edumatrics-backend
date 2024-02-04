import datetime
from attendanceManager.models import (
    TimeTable,
    StaffTimeTable,
    Student,
    Staff,
    LectureHall,
)

def convert_to_datetime(railway_time):
    normal_time = railway_time.strftime("%I:%M %p")
    return normal_time

def getStudentTimeTable(_class):
    data = []

    _class = _class.split()
    classes = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
    }

    print(
        "class in lecture_hall.serializers: ",
        str(classes[_class[0]]) + " " + " - ".join(_class[1:]),
    )
    try:
        l = LectureHall.objects.get(
            className=str(classes[_class[0]]) + " " + " - ".join(_class[1:])
        )

        timetable_objects = TimeTable.objects.filter(Class=l)

        days = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
        ]

        raw_data = {
            "monday": [],
            "tuesday": [],
            "wednesday": [],
            "thursday": [],
            "friday": [],
            "saturday": [],
        }

        timings = []
        for i in timetable_objects:
            t = i.returnData()
            raw_data[t["day"]] += [
                [t["day"], int(t["hour"]), t["period"], t["start"], t["end"]]
            ]
            timings += [f"{convert_to_datetime(t["start"])} - {convert_to_datetime(t["end"])}"]
        
        k = 0
        while k < 7:
            data.append(timings[k])
            print(timings[k])
            for i in days:
                try:
                    data.append(raw_data[i][k][2])
                except Exception as e:
                    pass
            k += 1
    except Exception as e:
        print("Exception in lecture_hall.serializers: ", e)

    print(len(data))
    return data

def getStaffTimeTable(name):
    data = {"monday": [],"tuesday": [],"wednesday": [],"thursday": [],"friday": [],"saturday": [],}
    try:
        staff = Staff.objects.get(name=name)
        rawData = StaffTimeTable.objects.filter(staffName=staff.id)
        print("rawData", rawData, "list(data.keys())", list(data.keys()))
        for i in rawData:
            temp = i.returnData()
            if temp['day'] in list(data.keys()):
                data[temp['day']] += [[temp['class'].first().className, temp["course"], str(convert_to_datetime(temp["start"])) + " - "+ str(convert_to_datetime(temp["start"]))]]
            else:
                data[temp['day']] = [[temp['class'].first().className, temp["course"], str(convert_to_datetime(temp["start"])) + " - "+ str(convert_to_datetime(temp["start"]))]]
        
        temp = data.copy()
        
        for i in data:
            print("data[i] == []", data[i] == [])
            if data[i] == []:
                temp.pop(i)
     
        print("temp", temp)
        data = temp
     
    except Exception as e:
        print("Exception in lecture_hall.serializers: ", e)
    print(data)
    print(len(data))
    return data

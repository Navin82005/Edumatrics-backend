from django.db import models
from auth_api.models import Student, Staff


class LectureHall(models.Model):
    names = models.ManyToManyField(to=Student, related_name="student_lecture_hall")
    className = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.className


class TimeTable(models.Model):
    # DATA
    # 08:30-09:30=DBMS||09:30-10:30=VERBAL||10:50-11:50=DM||11:50-12:50=MPMC||[01:40-02:40,02:40-03:25,03:45-04:30]=MPMC LAB

    # name = models.CharField(max_length=255, blank=True, null=True)
    # Class = models.OneToOneField(to=LectureHall, on_delete=models.CASCADE, null=True)
    # monday = models.CharField(max_length=355, blank=True, null=True)
    # tuesday = models.CharField(max_length=355, blank=True, null=True)
    # wednesday = models.CharField(max_length=355, blank=True, null=True)
    # thursday = models.CharField(max_length=355, blank=True, null=True)
    # friday = models.CharField(max_length=355, blank=True, null=True)
    # saturday = models.CharField(max_length=355, blank=True, null=True)

    Class = models.ManyToManyField(to=LectureHall)
    day = models.CharField(max_length=30, null=True)
    hour = models.CharField(max_length=30, null=True)
    period = models.CharField(max_length=255, null=True)
    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(null=True, blank=True)
    classname = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        self.classname = str(self.Class.first())
        self.save()
        return (
            str(self.Class.first())
            + " "
            + str(self.day).capitalize()
            + " "
            + str(self.hour)
            + " Time Table"
        )

    class Meta:
        ordering = ["classname", "day", "hour"]

    def returnData(self):
        return {
            "day": self.day,
            "hour": self.hour,
            "period": self.period,
            "start": self.start,
            "end": self.end,
        }


class StaffTimeTable(models.Model):
    staffName = models.ManyToManyField(to=Staff)
    Class = models.ManyToManyField(to=LectureHall)
    day = models.CharField(max_length=30, null=True)
    hour = models.CharField(max_length=30, null=True)
    course = models.CharField(max_length=255, null=True)
    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(null=True, blank=True)

    def __str__(self):
        return (
            str(self.staffName.first()).capitalize()
            + " "
            + str(self.Class.first())
            + " "
            + str(self.day).capitalize()
            + " "
            + str(self.course)
        )

    def returnData(self):
        return {
            "day": self.day,
            "class": self.Class,
            "hour": self.hour,
            "course": self.course,
            "start": self.start,
            "end": self.end,
        }

    class Meta:
        ordering = ["day", "hour"]


class ClassSession(models.Model):
    period = models.ManyToManyField(to=TimeTable)
    date = models.DateField(blank=True, null=True, auto_now_add=True)
    isPresent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)


class LectureHallAttadence(models.Model):
    Class = models.ManyToManyField(to=LectureHall)
    name = models.ManyToManyField(to=Student)
    h1 = models.CharField(max_length=255, null=True, blank=True)
    h2 = models.CharField(max_length=255, null=True, blank=True)
    h3 = models.CharField(max_length=255, null=True, blank=True)
    h4 = models.CharField(max_length=255, null=True, blank=True)
    h5 = models.CharField(max_length=255, null=True, blank=True)
    h6 = models.CharField(max_length=255, null=True, blank=True)
    h7 = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True)
    mainName = models.CharField(max_length=255, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     self.mainName = str(self.name.first())
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name.first()} - {self.date}"

    class Meta:
        ordering = ["date", "mainName"]

    def returnPeriods(self):
        return {
            1: self.h1,
            2: self.h2,
            3: self.h3,
            4: self.h4,
            5: self.h5,
            6: self.h6,
            7: self.h7,
        }

    def returnData(self):
        return {
            "date": self.date,
            "mainName": self.mainName,
            "class": self.Class,
        }

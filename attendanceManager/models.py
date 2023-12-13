from django.db import models
from auth_api.models import Student

class LectureHall(models.Model):
    names = models.ManyToManyField(to=Student, related_name='student_lecture_hall')
    className = models.CharField(max_length=255, blank=True)

    # def save(self, *args, **kwargs):
    #     pass

    def __str__(self):
        return self.className

class Periods(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class ClassSession(models.Model):
    period = models.ManyToManyField(to=Periods)
    date = models.DateField(blank=True, null=True, auto_now_add=True)
    isPresent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)

class LectureHallAttadence(models.Model):
    user = models.ManyToManyField(to=LectureHall)
    name = models.CharField(max_length=255, null=True)
    classSession = models.ManyToManyField(to=ClassSession)
    # for u in user.name:
    #     u = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' Attendance'

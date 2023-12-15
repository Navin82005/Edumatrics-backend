from django.db import models
from auth_api.models import Student


class LectureHall(models.Model):
    names = models.ManyToManyField(to=Student, related_name="student_lecture_hall")
    className = models.CharField(max_length=255, blank=True)

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


    def save(self, *args, **kwargs):
        self.mainName = str(self.name.first())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name.first()} - {self.date}"

    class Meta:
        ordering = ["date", "mainName"]

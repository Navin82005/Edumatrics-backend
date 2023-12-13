from django.db import models
from auth_api.models import Student

class LectureHall(models.Model):
    names = models.ManyToManyField(to=Student, related_name='student_lecture_hall')
    className = models.CharField(max_length=255, blank=True)

    # def save(self, *args, **kwargs):
    #     pass

    def __str__(self):
        return self.className

class Attadence(models.Model):
    user = models.OneToOneField(to=Student, on_delete=models.CASCADE)
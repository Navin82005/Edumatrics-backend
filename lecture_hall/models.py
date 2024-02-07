from django.db import models
from attendanceManager.models import LectureHall


# Create your models here.
class Subject(models.Model):
    _lh = models.ManyToManyField(to=LectureHall)
    subjectName = models.CharField(max_length=255, blank=True)
    subjectCode = models.CharField(max_length=255, blank=True)
    subjectType = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.subjectName) + " -> " + str(self._lh.first())

    class Meta:
        ordering = ["subjectName"]

    def returnData(self):
        return {
            "class": self._lh,
            "subject": self.subjectName,
        }

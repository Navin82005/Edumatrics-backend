from django.db import models
from django.contrib.auth.models import User, AbstractUser
import bcrypt


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.username.first_name

class Staff(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    isAdvisor = models.BooleanField(default=False)
    lectureHall = models.CharField(max_length=30, blank=True)
    userMobile = models.CharField(max_length=30, blank=True)
    userDob = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

    def get_main_data(self):
        return {
            "username": self.username,
            "name": self.name,
            "isAdvisor": self.isAdvisor,
            "lectureHall": self.lectureHall,
            "userMobile": self.userMobile,
            "userDob": self.userDob,
        }


class Student(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    rollNumber = models.CharField(max_length=8, blank=True)
    registerNumber = models.CharField(max_length=15, blank=True)
    name = models.CharField(max_length=50, blank=True)
    sem = models.CharField(max_length=50, blank=True)
    lectureHall = models.CharField(max_length=30, blank=True)
    userMobile = models.CharField(max_length=30, blank=True)
    userDob = models.CharField(max_length=30, blank=True)
    profile_picture = models.FileField(upload_to="images/profiles", blank=True)
    department = models.CharField(max_length=225, blank=True)
    inClass = models.CharField(max_length=225, blank=True)
    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.name

    def get_main_data(self):
        return {
            # "username": self.username,
            "name": self.name,
            "rollNo": self.rollNumber,
            "regNo": self.registerNumber,
            "lectureHall": self.lectureHall,
            "userMobile": self.userMobile,
            "userDob": self.userDob,
            "department": self.department,
        }

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), (self.password).encode("utf-8"))


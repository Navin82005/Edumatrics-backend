from django.db import models
from django.contrib.auth.models import User


class Admins(models.Model):
    email_username = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Admin " + self.name

    def get_main_data(self):
        return {
            "email_username": self.email_username,
            "name": self.name,
        }

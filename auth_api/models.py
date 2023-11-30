from django.db import models
from django.contrib.auth.models import User, AbstractUser
import bcrypt


# Create your models here.
class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=6255)
    password_is_hashed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # CREATING HASH FOR THE PASSWORD
        if not self.password_is_hashed:
            encoded_password = (self.password).encode("utf-8")
            salt = bcrypt.gensalt()
            self.password = bcrypt.hashpw(encoded_password, salt)
            self.password = self.password.decode("utf-8")
            self.password_is_hashed = True
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), (self.password).encode("utf-8"))

    @classmethod
    def authenticate(cls, username, password):
        try:
            user = cls.objects.get(username=username)
            if user.check_password(password):
                return user
        except cls.DoesNotExist:
            return None
        
        return None


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=6255)
    password_is_hashed = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # CREATING HASH FOR THE PASSWORD
        if not self.password_is_hashed:
            encoded_password = (self.password).encode("utf-8")
            salt = bcrypt.gensalt()
            self.password = bcrypt.hashpw(encoded_password, salt)
            self.password = self.password.decode("utf-8")
            self.password_is_hashed = True
            super().save(*args, **kwargs)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), (self.password).encode('utf-8'))

    @classmethod
    def authenticate(cls, username, password):
        try:
            user = cls.objects.get(username=username)
            if user.check_password(password):
                return user
        except cls.DoesNotExist:
            return None
        
        return None
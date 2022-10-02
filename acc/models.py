from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser): # AbstractBaseUser 아니에요
    pic = models.ImageField(upload_to="user")
    comment = models.TextField()
    point = models.IntegerField(default=0)

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.png"


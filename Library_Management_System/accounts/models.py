from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class LibraryUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    department = models.CharField(max_length=100,blank=True,null=True)


class Book(models.Model):
    pass



class Issue(models.model):
    pass



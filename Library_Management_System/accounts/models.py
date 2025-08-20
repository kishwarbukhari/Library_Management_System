from django.db import models
from django.contrib.auth.models import AbstractUser


class LibraryUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    department = models.CharField(max_length=100,blank=True,null=True)


    



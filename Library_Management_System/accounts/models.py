from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    department = models.CharField(max_length=100,blank=True,null=True)


class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=200)
        category = models.CharField(max_length=100)
        isbn = models.CharField(max_length=20, unique=True)
        satus = models.BooleanFieldd(default=True)

        def __str__(self):
            return self.title
        



class Issue(models.model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField( auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=False)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
    
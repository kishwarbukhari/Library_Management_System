from django.db import models
from django.contrib.auth.models import User 



class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=200)
        category = models.CharField(max_length=100)
        isbn = models.CharField(max_length=20, unique=True)
        status = models.BooleanField(default=True)

        def __str__(self):
            return self.title
        


class Issue(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField( auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.student.username} - {self.book.title}"

    
from django.contrib import admin
from .models import Book, Issue


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'isbn', 'status')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('category', 'status')

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('student', 'book', 'issue_date', 'due_date', 'return_date', 'fine')
    search_fields = ('student__username', 'book__title')
    list_filter = ('issue_date', 'due_date', 'return_date')


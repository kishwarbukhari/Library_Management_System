from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from .import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.accounts, name='accounts'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('librarian-dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
]

from django.urls import path
from . import views

urlpatterns=[
    path('students/',views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    path('employees/',views.Employees.as_view()),#for Class Based Views
    path('employees/<int:pk>/',views.EmployeeDetail.as_view()),#for Accessing a  single Employee


]




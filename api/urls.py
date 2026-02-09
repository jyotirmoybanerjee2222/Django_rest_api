from django.urls import path,include
from . import views
#for ViewSet
from rest_framework.routers import DefaultRouter 
router=DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='employee')
#router = DefaultRouter('empolyees',views.EmployeeViewset,basename='employee')

urlpatterns=[
    path('students/',views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    # path('employees/',views.Employees.as_view()),#for Class Based Views
    # path('employees/<int:pk>/',views.EmployeeDetail.as_view()),#for Accessing a  single Employee
    path('',include(router.urls)),

    #for blogs
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),

    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailView.as_view())



]




from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
# Create your views here.
def studentsView(req):
     #return Student data
    # students =[
    #     {'id':1,'name':'John Doe','class':'computer Science','age':25}
    # ]
    # return JsonResponse(students,safe=False)

    #return Student model
    students = Student.objects.all()
    ## Manual serializations
    students_list = list(students.values())
    print(students)
    return JsonResponse(students_list,safe=False)
    





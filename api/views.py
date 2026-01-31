from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def studentsView(request):
     #return Student data
    # students =[
    #     {'id':1,'name':'John Doe','class':'computer Science','age':25}
    # ]
    # return JsonResponse(students,safe=False)

    #return Student model
    # students = Student.objects.all()
    ## Manual serializations
    # students_list = list(students.values())
    # print(students)
    # return JsonResponse(students_list,safe=False)

    #function based view get Method
    if request.method == 'GET':
        #get all the data from Student Table
        student = Student.objects.all()
        serializer = StudentSerializer(student,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    





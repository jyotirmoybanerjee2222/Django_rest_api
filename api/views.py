from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
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
    #Storing Data using Serializations
    elif request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def studentDeatailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)#get a singlee object Primary Key Based Operations 
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    


    





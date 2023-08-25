from django.shortcuts import render
from fbvApp.serializer import StudentSerializer
from fbvApp.models import Student
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def student_list(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':

        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def student_details(request,pk):

    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response("Student Does not Exist",status=status.HTTP_404_NOT_FOUND) 
        
        
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    



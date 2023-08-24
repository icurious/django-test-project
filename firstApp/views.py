from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee
from rest_framework.response import Response  
# Create your views here.

def get_employee(request):
    emp = { 
        "id": 123, 
        "name": "DJ", 
        "Salary": 50000
        }

    data = list(Employee.objects.all().values())

    return JsonResponse({'data': data})

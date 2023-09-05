from ast import Pass
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from passenger.models import Passengers
from passenger.serializer import PassengersSerializer

# Create your views here.

@api_view(["GET", "POST"])
def passengers_list(request):

    if request.method == 'GET':
        passengers_list = Passengers.objects.all()
        serializer = PassengersSerializer(passengers_list,many=True)
        return Response({"passengers": serializer.data},status.HTTP_200_OK) 
    
    elif request.method == 'POST':
        serializer = PassengersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def passenger_info(request,pk):

    try:
        passenger = Passengers.objects.get(pk=pk)
    except Passengers.DoesNotExist:
        return Response({"message": "Passenger does not exists"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PassengersSerializer(passenger)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    elif request.method == "PUT":
        serializer = PassengersSerializer(passenger,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



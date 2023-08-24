
from django.urls import path
from firstApp import views

urlpatterns = [
    
    path("employee", views.get_employee,name="get_employee")
]

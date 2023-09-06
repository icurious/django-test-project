from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)



class Books(models.Model):
    title = models.CharField(max_length=250)
    rating = models.CharField(max_length=20)
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)

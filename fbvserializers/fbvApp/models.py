from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    score = models.IntegerField()


    def __str__(self) -> str:
        return "id: {}  name: {} score: {}".format(self.id, self.name, self.score)
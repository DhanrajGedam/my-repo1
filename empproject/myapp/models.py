from django.db import models
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=20)
    email=models.EmailField()
    edoj=models.DateField()
    edesig=models.CharField(max_length=20)
    eexp=models.FloatField()
    ecompany=models.CharField(max_length=20)
    esal=models.IntegerField()
    def __str__(self):
        return self.ename
# Create your models here.

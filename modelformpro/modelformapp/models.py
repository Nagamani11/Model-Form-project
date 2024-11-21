from django.db import models

class EmpData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    salary = models.IntegerField()
    location = models.CharField(max_length=50)

from django.db import models

# Create your models here.
class Person(models.Model):
    name    = models.CharField(max_length = 20)#max_field is required
    surname = models.CharField(max_length = 20)
    dob     = models.DateField()
    description = models.TextField()
    summary = models.TextField(default = 'this beech')
    employed = models.BooleanField()

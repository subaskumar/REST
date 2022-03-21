from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

def rollNO_limit(value):
    if value > 200:
        raise ValidationError(" The Seat is full %(value)s", params={'value': value})
class Student(models.Model):
    name = models.CharField(max_length=120)
    roll = models.IntegerField(validators=[rollNO_limit])
    city = models.CharField(max_length=120)
    
    def __str__(self):
        return str(self.name)
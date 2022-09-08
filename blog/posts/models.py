from statistics import mode
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Fruit(models.Model):
  name = models.CharField(max_length=15)
  description = models.CharField(max_length=150)
  price_per_kg = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(20)])
  
  def __str__(self):
      return f'{self.name} : {self.description}'
  

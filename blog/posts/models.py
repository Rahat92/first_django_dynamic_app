from pyexpat import model
from statistics import mode
from turtle import ondrag
from unicodedata import category
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import  slugify
# Create your models here.

class Category(models.Model):
  category = models.CharField(null = True,max_length=50)

class Fruit(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
  name = models.CharField(max_length=20)
  description = models.CharField(max_length=150)
  price_per_kg = models.IntegerField(null = True,validators=[MinValueValidator(10),MaxValueValidator(20)])
  image = models.ImageField(blank =True, null = True)
  slug =models.SlugField(default="", editable=False, db_index= True, null=False, blank=True)
  def get_absolute_url(self):
    return reverse("post", args=[self.slug])
    # return reverse("post", kwargs={"pk":self.pk})
  # def save(self,*args, **kwargs):
  #   self.slug = slugify(self.name)
  #   super().save(*args,**kwargs)
    
  def __str__(self):
    return f'{self.name} : {self.description} , price per kg: {self.price_per_kg}'


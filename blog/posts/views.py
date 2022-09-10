from django.shortcuts import render
# from django.http import HttpResponse 
# from django.template.loader import render_to_string
from .models import Fruit
def index(request):
  fruits = Fruit.objects.all()
  return render(request,'posts/index.html',{
    'fruits':fruits
  })
  
def post(request,slug): #id == name
  # description = []
  # for singlePost in fruits:
  #   if (singlePost['name'] == name):
  #     description.append(singlePost)
  fruit = Fruit.objects.get(slug = slug)
  return render(request,'posts/post.html',{
    'fruit':fruit,
  })


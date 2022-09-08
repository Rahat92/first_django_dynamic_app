from django.shortcuts import render
from django.http import HttpResponse 
# from django.template.loader import render_to_string
from django.utils.text import slugify
# Create your views here.

fruits = [
  {
    'name':'আম',
    'description':'আম হল ফলের রাজা !'
  },
  {
    'name':'কমলা',
    'description':'কমলাতে থাকে ভিটামিন সি ।'
  },
  {
    'name':'কাঠাল',
    'description':'কাঠাল আমাদের জাতীয় ফল।'
  },
]

def index(request):
  return render(request,'posts/index.html',{
    'fruits':fruits
  })

def post(request,name):
  description = []
  for singlePost in fruits:
    if (singlePost['name'] == name):
      description.append(singlePost)
  return render(request,'posts/post.html',{
    'fruit':description[0],
    'name':name
  })


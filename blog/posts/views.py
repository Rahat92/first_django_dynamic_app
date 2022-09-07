from django.shortcuts import render
from django.http import HttpResponse 
# from django.template.loader import render_to_string
from django.utils.text import slugify
# Create your views here.

all_posts = [
  {
    'postTitle':'কলা',
    'postDetail':'আম হল ফলের রাজা'
  },
  {
    'postTitle':'আম',
    'postDetail':'কলাতে থাকে অনেক ভিটামিন ।'
  },
  {
    'postTitle':'কমলা',
    'postDetail':'কমলাতে থাকে ভিটামিন সি ।'
  },
  {
    'postTitle':'কাঠাল',
    'postDetail':'কাঠাল আমাদের জাতীয় ফল।'
  },
  
]

def index(request):
  return render(request,'posts/index.html',{
    'all_posts':all_posts
  })

def post(request,title):
  postDetail = []
  for singlePost in all_posts:
    if (singlePost['postTitle'] == title):
      postDetail.append(singlePost)
  return render(request,'posts/post.html',{
    'post':postDetail[0],
    'title':title
  })


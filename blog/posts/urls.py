from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.index,),
    path('<str:title>',views.post, name = 'post'),
]
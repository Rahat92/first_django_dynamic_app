from django.urls import path
from . import views
urlpatterns = [ 
    path('main/',views.index, name = 'index' ),
    path('main/<str:name>',views.post, name = 'post'),
]

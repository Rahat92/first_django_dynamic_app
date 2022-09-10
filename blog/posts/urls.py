from django.urls import path
from . import views
urlpatterns = [ 
    path('main/',views.index, name = 'index' ),
    path('main/<slug:slug>',views.post, name = 'post'),
]

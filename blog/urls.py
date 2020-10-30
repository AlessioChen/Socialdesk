from django.urls import path
from . import views 

urlpatterns = [
  path('', views.home, name = 'blog-home'),
  path('new-post/', views.post, name ='new-post'),
  
  
]

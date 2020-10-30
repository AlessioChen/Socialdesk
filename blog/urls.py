from django.urls import path
from . import views 

urlpatterns = [
  path('', views.home, name = 'blog-home'),
  path('new-post/', views.new_post, name ='new-post'),
  
  
]

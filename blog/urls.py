from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('new-post/', views.new_post, name='new-post'),
    path('user_posts_count/', views.user_posts_count, name='user_posts_count'),

]

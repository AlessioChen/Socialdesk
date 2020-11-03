from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('new-post/', views.new_post, name='new-post'),
    path('user_posts_count/', views.user_posts_count, name='user_posts_count'),
    path('last_hour_posts/', views.last_hour_posts, name = 'last_hour_posts'), 
    path('word_count/', views.word_count, name = 'word_count'),

]

from django.urls import path
from likes import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('like/post/<post_id>/', views.like, name='like'),
    path('dislike/post/<post_id>/', views.dislike, name='dislike'),
]

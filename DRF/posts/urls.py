from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import  PostList, PostDetail
from .views import UserList, UserDetail
from . import views



urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()), 

    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),

]



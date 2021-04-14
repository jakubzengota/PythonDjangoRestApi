from django.shortcuts import render

from django.contrib.auth import get_user_model 
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Ksiazka

from .permissions import IsAuthorOrReadOnly
from .serializers import KsiazkaSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
    class KsiazkaList(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,IsAuthenticated)
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']
# Create your views here.

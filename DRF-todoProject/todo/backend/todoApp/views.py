from django.shortcuts import render
from rest_framework import generics
from . import models
from .serializers import TodoSerializer
# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

from django.shortcuts import render,redirect
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
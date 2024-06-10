from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer




class ActionViewset(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ = 'action')
    serializer_class = MovieSerializer


class ComedyViewset(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ = 'comedy')
    serializer_class = MovieSerializer
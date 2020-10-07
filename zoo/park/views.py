from django.db import models
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Animal, Employee, Category, CarePeriod, Space
from .serializers import (
    AnimalListSerializer,
    SpaceListSerializer,
)
from .service import AnimalFilter, SpaceFilter

class AnimalListView(generics.ListAPIView):
    """Вывод списка фильмов"""
    serializer_class = AnimalListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter
    queryset = Animal.objects.all()


class SpaceListView(generics.ListAPIView):
    """Вывод списка вольеров"""
    serializer_class = SpaceListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SpaceFilter
    queryset = Space.objects.all()

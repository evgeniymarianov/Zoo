from django.db import models
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Animal, Employee, Category, CarePeriod, Space
from .serializers import (
    AnimalListSerializer,
    SpaceListSerializer,
)
from .service import AnimalFilter, SpaceFilter, AnimalFilter2
from rest_framework.generics import CreateAPIView, ListAPIView
from django.db.models import Count

class AnimalListView(generics.ListAPIView):
    """Вывод списка животных"""
    serializer_class = AnimalListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter
    queryset = Animal.objects.all()


class SpaceListView(generics.ListAPIView):
    """Вывод списка вольеров у которых число животных больше чем 'q' """
    serializer_class = SpaceListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SpaceFilter

    def get_queryset(self, *args, **kwargs):
        queryset_list = Space.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = Space.objects.annotate(num_animals=Count('animals')).filter(num_animals__gt=query)
        print(queryset_list)
        return queryset_list


class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter2
    queryset = Animal.objects.all()

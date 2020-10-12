from django.db import models
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Animal, Employee, Category, CarePeriod, Space
from .serializers import (
    AnimalListSerializer,
    SpaceListSerializer,
)
from .service import SpaceFilter, AnimalFilter
from rest_framework.generics import CreateAPIView, ListAPIView
from django.db.models import Count

#class AnimalListView(generics.ListAPIView):
#    """Вывод списка животных"""
#    serializer_class = AnimalListSerializer
#    filter_backends = (DjangoFilterBackend,)
#    filterset_class = AnimalFilter
#    queryset = Animal.objects.all()


class SpaceListView(generics.ListAPIView):
    """Вывод списка вольеров у которых видов животных больше чем 2 """
    serializer_class = SpaceListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SpaceFilter
    queryset = Space.objects.all()

#    def get_queryset(self, *args, **kwargs):
#        queryset_list = Space.objects.all()
#        more_than_two_categories = self.request.query_params.get('more_than_two_categories', '')
#        if more_than_two_categories:
#            if more_than_two_categories == 'True':
#                queryset_list = Space.objects.annotate(num_categories=Count('categories')).filter(num_categories__gt=2)
#                return queryset_list
#        print(queryset_list)
#        return queryset_list


class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter
    queryset = Animal.objects.all()

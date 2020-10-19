from django.db import models
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Animal, Employee, Category, CarePeriod, Space
from .serializers import (
    AnimalListSerializer,
    SpaceListSerializer,
    CategoryListSerializer,
    EmployeeListSerializer,
    AnimalCreateSerializer,
    SpaceSerializer,
    CategorySerializer,
    #AnimalSerializer,
    #EmployeeSerializer,
)
from .service import SpaceFilter, AnimalFilter, EmployeesAnimalFilter, CategoryFilter
from rest_framework.generics import CreateAPIView, ListAPIView
from django.db.models import Count
from datetime import timedelta
from django.db.models import F
from datetime import datetime, date
from django.utils import timezone
from rest_framework import mixins


class SpaceList(generics.ListCreateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SpaceFilter


class SpaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


class CategoryListView(generics.ListAPIView):
    """Вывод списка вольеров по параметрам животных"""
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    queryset = Category.objects.all()


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    queryset = Category.objects.all()
    filterset_class = CategoryFilter


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """Вывод списка животных по параметрам вольера"""
    serializer_class = AnimalListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter
    queryset = Animal.objects.all()


class AnimalOfEmployeeViewSet(AnimalViewSet):
    """Вывод списка животных, за которыми закреплен один и тот же \n
    сотрудник более 1 года."""
    filterset_class = EmployeesAnimalFilter

    def get_queryset(self, *args, **kwargs):
        employee_id = self.request.query_params.get('careperiods__employee', '')
        if employee_id:
            employee = Employee.objects.get(id=employee_id)
            queryset_list = Animal.objects.filter(
            careperiods__created_at__gt=datetime.now()-timedelta(days=365),
            careperiods__ended_at__isnull=True,
            careperiods__employee=employee
            ).distinct()
            return queryset_list
        queryset_list = Animal.objects.all()
        return queryset_list


class AnimalCreateViewSet(viewsets.ModelViewSet):
    """Добавление животного"""
    serializer_class = AnimalCreateSerializer


class EmployeeListView(generics.ListAPIView):
    """Вывод списка вольеров по параметрам животных"""
    serializer_class = EmployeeListSerializer
    filter_backends = (DjangoFilterBackend,)
    queryset = Employee.objects.all()

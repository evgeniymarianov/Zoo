from django.db import models
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Animal, Employee, Category, CarePeriod, Space
from .serializers import (
    SpaceSerializer,
    CategorySerializer,
    AnimalSerializer,
    EmployeeSerializer,
)
from .service import SpaceFilter, AnimalFilter, EmployeesAnimalFilter, CategoryFilter, EmployeeFilter
from rest_framework.generics import CreateAPIView, ListAPIView
from django.db.models import Count
from datetime import timedelta
from django.db.models import F
from datetime import datetime, date
from django.utils import timezone
from rest_framework import mixins


class SpaceList(generics.ListCreateAPIView):
    """Создание вольера и вывод списка вольеров"""
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SpaceFilter


class SpaceDetail(generics.RetrieveUpdateDestroyAPIView):
    """Вывод, редакция, удаление вольеров"""
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer


class CategoryList(generics.ListCreateAPIView):
    """Создание категории и вывод списка категорий"""
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    queryset = Category.objects.all()
    filterset_class = CategoryFilter


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """Вывод, редакция, удаление категории"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AnimalList(generics.ListCreateAPIView):
    """Создание животного или вывод списка животных по параметрам вольера"""
    serializer_class = AnimalSerializer
    filter_backends = (DjangoFilterBackend,)
    queryset = Animal.objects.all()
    filterset_class = AnimalFilter


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    """Вывод, редакция, удаление животного"""
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalOfEmployeeViewSet(AnimalList):
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


class EmployeeList(generics.ListCreateAPIView):
    """Создание сотрудника и вывод списка сотрудников"""
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend,)
    queryset = Employee.objects.all()
    filterset_class = EmployeeFilter


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """Вывод, редакция, удаление сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

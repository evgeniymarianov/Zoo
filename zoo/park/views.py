from django.db import models
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Animal, Employee, Category, CarePeriod, Space
from .serializers import (
    AnimalListSerializer,
    SpaceListSerializer,
)
from .service import SpaceFilter, AnimalFilter, AnimalFilter2
from rest_framework.generics import CreateAPIView, ListAPIView
from django.db.models import Count
from datetime import timedelta
from django.db.models import F
from datetime import datetime, date
from django.utils import timezone


class SpaceListView(generics.ListAPIView):
    """Вывод списка вольеров по параметрам животных"""
    serializer_class = SpaceListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SpaceFilter
    queryset = Space.objects.all()


class AnimalViewSet(viewsets.ModelViewSet):
    """Вывод списка животных по параметрам вольера"""
    serializer_class = AnimalListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter
    queryset = Animal.objects.all()


class AnimalViewSet2(viewsets.ModelViewSet):
    """Вывод списка животных, за которыми закреплен один и тот же \n
    сотрудник более 1 года."""
    serializer_class = AnimalListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter2
    queryset = None

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

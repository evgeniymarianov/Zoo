from django_filters import rest_framework
from .models import Animal, Employee, Category, CarePeriod, Space
from django_filters.rest_framework import FilterSet, filters, CharFilter
from django.db.models import Avg, Count


class AnimalFilter(rest_framework.FilterSet):

    class Meta:
        model = Animal
        fields = '__all__'


class SpaceFilter(rest_framework.FilterSet):

    class Meta:
        model = Space
        fields = '__all__'

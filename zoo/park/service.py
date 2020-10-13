from django_filters import rest_framework
from .models import Animal, Employee, Category, CarePeriod, Space
from django_filters.rest_framework import FilterSet, filters, CharFilter, DateTimeFromToRangeFilter
from django.db.models import Avg, Count
from django import forms


class SpaceFilter(rest_framework.FilterSet):
    contains_more_than_n_categories = rest_framework.CharFilter(
        label=('Содержится видов животных больше чем n:'),
        method ="filter_by_categories_count"
    )

    class Meta:
        model = Space
        fields = [
        "name",
        "categories",
        "description",
        "illumination",
        "type",
        "square",
        "categories__animals__name",
        "categories__animals__description",
        "categories__animals__gender",
        "categories__animals__age",
        "categories__animals__created_at",
        "categories__animals__color",
        ]

    def filter_by_categories_count(self, queryset, name, value):
        queryset = Space.objects.annotate(num_categories=Count('categories')).filter(num_categories__gt=value)
        return queryset


class AnimalFilter(rest_framework.FilterSet):

    class Meta:
        model = Animal
        fields = [
            "category__space__name",
            "category__space__created_at",
            "category__space__description",
            "category__space__type",
            "category__space__square",
            "category__space__illumination",
           ]


class AnimalFilter2(rest_framework.FilterSet):
    careperiods__employee = filters.ModelChoiceFilter(
        label=('Закреплённый сотрудник'),
        queryset=Employee.objects.all()
    )
    # DurationFilter
    # careperiods__created_at__gt
    class Meta:
        model = Animal
        fields = ['name']

from django_filters import rest_framework
from .models import Animal, Employee, Category, CarePeriod, Space
from django_filters.rest_framework import FilterSet, filters, CharFilter
from django.db.models import Avg, Count


# class AnimalFilter(rest_framework.FilterSet):
#
#     class Meta:
#         model = Animal
#         fields = '__all__'


class SpaceFilter(rest_framework.FilterSet):


    class Meta:
        model = Space
        fields = '__all__'


class AnimalFilter2(rest_framework.FilterSet):
    careperiods = rest_framework.CharFilter(method ="filter_by_careperiods")
    space = filters.ModelChoiceFilter(queryset=Space.objects.annotate(num_animals=Count('categories')).filter(num_animals__gt=2))

    class Meta:
        model = Animal
        fields = ["name", "careperiods", "description", "space"]

    def filter_by_careperiods(self, queryset, name, value):
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(queryset)
        print(value)
        careperiods = CarePeriod.objects.all()
        return queryset

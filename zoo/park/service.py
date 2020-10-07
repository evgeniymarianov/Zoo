from django_filters import rest_framework
from .models import Animal, Employee, Category, CarePeriod, Space
from django_filters.rest_framework import FilterSet, filters
from django.db.models import Avg, Count


class AnimalFilter(rest_framework.FilterSet):

    class Meta:
        model = Animal
        fields = '__all__'


class SpaceFilter(rest_framework.FilterSet):
    #spaces = filters.ModelChoiceFilter(queryset=Space.objects.annotate(num_animals=Count('animals')).filter(num_animals__gt=2))
    #queryset = Space.objects.annotate(num_animals=Count('animals')).filter(num_animals__gt=2)
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    #print(animals)


    class Meta:
        model = Space
        #fields = '__all__'
        fields = ['min_price']

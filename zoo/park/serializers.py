from .models import Animal, Employee, Category, CarePeriod, Space, PlacementPeriod
from rest_framework import serializers


class CarePeriodSerializer(serializers.ModelSerializer):
    """Список периодов ухода за животными"""
    employee = serializers.SlugRelatedField(slug_field='firstname', read_only=True)
    animal = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = CarePeriod
        fields = "__all__"


class PlacementPeriodSerializer(serializers.ModelSerializer):
    """Список периодов размещения животных в вольерах"""
    category = serializers.SlugRelatedField(slug_field='firstname', read_only=True)
    space = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = PlacementPeriod
        fields = "__all__"


class AnimalListSerializer(serializers.ModelSerializer):
    """Список животных"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    #careperiods = serializers.SlugRelatedField(slug_field='created_at', read_only=True, many=True)
    careperiods = CarePeriodSerializer(many=True)

    class Meta:
        model = Animal
        fields = "__all__"


class AnimalCreateSerializer(serializers.ModelSerializer):
    """Добавление животного"""

    class Meta:
        model = Animal
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    """Список видов животных"""
    animals = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    space = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Category
        fields = "__all__"


class SpaceListSerializer(serializers.ModelSerializer):
    """Список вольеров"""
    placementperiods = PlacementPeriodSerializer(many=True)

    class Meta:
        model = Space
        fields = "__all__"


class EmployeeListSerializer(serializers.ModelSerializer):
    """Список сотрудников"""
    careperiods = serializers.SlugRelatedField(slug_field='created_at', read_only=True, many=True)

    class Meta:
        model = Employee
        fields = "__all__"


class SpaceSerializer(serializers.ModelSerializer):
    """Список вольеров"""
    placementperiods = PlacementPeriodSerializer(many=True)

    class Meta:
        model = Space
        fields = "__all__"

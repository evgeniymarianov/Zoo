from .models import Animal, Employee, Category, CarePeriod, Space
from rest_framework import serializers


class AnimalListSerializer(serializers.ModelSerializer):
    """Список животных"""

    class Meta:
        model = Animal
        fields = "__all__"


class SpaceListSerializer(serializers.ModelSerializer):
    """Список животных"""

    class Meta:
        model = Space
        fields = "__all__"

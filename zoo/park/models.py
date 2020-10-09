import datetime
from django.db import models
from datetime import date
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    """Категории животных"""
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    dangerous = models.BooleanField("Опасен для человека", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Space(models.Model):
    """Помещения животных"""
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    name = models.CharField("Название", max_length=100)
    type = models.CharField(choices = (
            ('Cage', 'Cage'),
            ('Enclosure', 'Enclosure'),
            ('Terrarium', 'Terrarium'),
        ),
        max_length=15, verbose_name=''
    )
    description = models.TextField("Описание")
    square = models.SmallIntegerField(null=False, verbose_name='Площадь')
    illumination = models.SmallIntegerField(null=False, verbose_name='Освящённость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Помещение"
        verbose_name_plural = "Помещения"

    def more_two(self):
        return self.objects.annotate(num_animals=Count('animals')).filter(num_animals__gt=2)


class Animal(models.Model):
    """Животные"""
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    gender = models.CharField(choices = (
            ('Female', 'Female'),
            ('Male', 'Male'),
        ),
        max_length=15)
    space = models.ForeignKey(Space, on_delete=models.PROTECT, related_name="animals")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"


class Employee(models.Model):
    """Сотрудники"""
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    firstname = models.CharField("Имя", max_length=100)
    lastname = models.CharField("Фамилия", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    animals = models.ManyToManyField(Animal)

    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class CarePeriod(models.Model):
    """Периоды ухода за животными животными"""
    created_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, related_name="careperiods")
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="careperiods")

    def duration_over_a_year(self):
        return self.created_at > timezone.now() - datetime.timedelta(days=365)

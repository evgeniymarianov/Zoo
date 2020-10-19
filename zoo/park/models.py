import datetime
from django.db import models
from datetime import date
from django.utils import timezone
from django.urls import reverse


class Space(models.Model):
    """Места для видов животных"""
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    name = models.CharField("Название", max_length=100)
    type = models.CharField(choices = (
            ('Cage', 'Cage'),
            ('Enclosure', 'Enclosure'),
            ('Terrarium', 'Terrarium'),
        ),
        max_length=15, verbose_name='Тип помещения'
    )
    description = models.TextField("Описание")
    square = models.SmallIntegerField(null=False, verbose_name='Площадь')
    illumination = models.SmallIntegerField(null=False, verbose_name='Освящённость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def more_two(self):
        return self.objects.annotate(num_categories=Count('categories')).filter(num_categories__gt=2)


class Category(models.Model):
    """Категории животных"""
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    dangerous = models.BooleanField("Опасен для человека", default=False)
    flying = models.BooleanField("Летающий", default=False)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


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
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.PROTECT, related_name="animals")
    color = models.CharField(null=True, choices = (
            ('Orange', 'Orange'),
            ('Black', 'Black'),
            ('White', 'White'),
            ('Brown', 'Brown'),
            ('Grey', 'Grey'),
        ),
        max_length=15)

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
    gender = models.CharField(choices = (
            ('Female', 'Female'),
            ('Male', 'Male'),
        ),
        max_length=15,
        default='Male')

    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class CarePeriod(models.Model):
    """Периоды ухода за животными"""
    created_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True, default=None)
    updated_at = models.DateTimeField()
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, related_name="careperiods")
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="careperiods")

    def continues_more_than_n_days(self, n=365):
        return not self.ended_at and self.created_at > timezone.now() - datetime.timedelta(days=n)

    def continues_less_than_n_days(self, n=365):
        return not self.ended_at and self.created_at < timezone.now() - datetime.timedelta(days=n)

    class Meta:
        verbose_name = "Период ухода"
        verbose_name_plural = "Периоды ухода"

class PlacementPeriod(models.Model):
    """Периоды размещения животных в вольерах"""
    created_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="placementperiods")
    space = models.ForeignKey(Space, on_delete=models.PROTECT, related_name="placementperiods")

    def continues_more_than_n_days(self, n=365):
        return not self.ended_at and self.created_at > timezone.now() - datetime.timedelta(days=n)

    def continues_less_than_n_days(self, n=365):
        return not self.ended_at and self.created_at < timezone.now() - datetime.timedelta(days=n)

    class Meta:
        verbose_name = "Период размещения"
        verbose_name_plural = "Периоды размещения"

from django.contrib import admin

from .models import Animal, Employee, Category, CarePeriod, Space

admin.site.register(Animal)
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(CarePeriod)
admin.site.register(Space)

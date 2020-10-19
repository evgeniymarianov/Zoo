from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('spaces/', views.SpaceList.as_view()),
    path('spaces/<int:pk>/', views.SpaceDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('animals/', views.AnimalList.as_view()),
    path('animals/<int:pk>/', views.AnimalDetail.as_view()),
    path('animals_of_employee/', views.AnimalOfEmployeeViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

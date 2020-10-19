from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    #path('animals/', views.AnimalListView.as_view()),
    #path('spaceso/', views.SpaceListView.as_view()),
    path('spaces/', views.SpaceList.as_view()),
    path('spaces/<int:pk>/', views.SpaceDetail.as_view()),
    #path('categories/', views.CategoryListView.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('employees/', views.EmployeeListView.as_view()),
    path('animals/', views.AnimalViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('animals_of_employee/', views.AnimalOfEmployeeViewSet.as_view({'get': 'list'})),
    #path('gift/<int:pk>/', views.GiftViewSet.as_view({'get': 'retrieve'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)

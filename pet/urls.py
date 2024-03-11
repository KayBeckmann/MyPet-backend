from django.urls import path
from .views import OwnerList, OwnerDetail, AnimalList, AnimalDetail

urlpatterns = [
    path('owner/',  OwnerList.as_view()),
    path('owner/<int:pk>',  OwnerDetail.as_view()),
    path('animal/',  AnimalList.as_view()),
    path('animal/<int:pk>',AnimalDetail.as_view()),
]
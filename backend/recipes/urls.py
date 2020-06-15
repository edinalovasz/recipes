from django.contrib import admin
from django.urls import path
from .views import GetPatchRecipes, ListPostRecipes, DeleteRecipes

urlpatterns = [
    path('<int:pk>/', GetPatchRecipes.as_view()),
    path('', ListPostRecipes.as_view()),
    path('delete/<int:pk>/', DeleteRecipes.as_view())
]


from django.urls import path
from .views import MealPlansView

urlpatterns = [
    path('mealsplans', MealPlansView.as_view()),
]


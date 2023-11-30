
from django.urls import path
from .views import HomePageView, TrainerList

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='trainer_list'),
    path('pokemon-card', TrainerList.as_view(), name='pokemon-card'),
    path('collection', TrainerList.as_view(), name='collection'),
]

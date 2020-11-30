from django.urls import path
from .views import GetAvailableTrains

urlpatterns = [
    path('availtrains/', GetAvailableTrains.as_view()),

]

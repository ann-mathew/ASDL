from django.urls import path
from .views import GetAvailableTrains, BookTicketView

urlpatterns = [
    path('availtrains/', GetAvailableTrains.as_view()),
    path('bookticket/', BookTicketView.as_view()),
]

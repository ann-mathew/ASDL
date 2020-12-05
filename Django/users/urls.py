from django.urls import path
from .views import UserRegister, UserLogin, GetBookings

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('login/', UserLogin.as_view()),
    path('bookings/', GetBookings.as_view()),
]

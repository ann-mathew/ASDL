from django.urls import path
from .views import UserRegister, UserLogin, GetBookings, GetUserData

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('login/', UserLogin.as_view()),
    path('get_user_data/', GetUserData.as_view()),
    path('user_bookings_history/', GetBookings.as_view()),
    
]

from django.urls import path
from .views import (UserRegister, UserLogin, GetBookings, GetUserData, SetUserDataView, DeleteUserView)

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('login/', UserLogin.as_view()),
    path('get_user_data/', GetUserData.as_view()),
    path('set_user_data/', SetUserDataView.as_view()),
    path('delete_user/', DeleteUserView.as_view()),
    path('user_bookings_history/', GetBookings.as_view()),
    
]

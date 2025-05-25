from django.urls import path, include
from .views import user_list, booking_list

urlpatterns = [
    path('', user_list, name='user_list'),
    path('bookings/', booking_list, name='booking_list'),
    path('api/', include('core.api')),
]

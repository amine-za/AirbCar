from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Booking
from rest_framework import viewsets
from .serializers import UserSerializer, BookingSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def user_list(request):
    users = User.objects.all()
    if not users:
        return HttpResponse("No Users found.")
    greetings = [f"Hi my name is {user.username}, with the id {user.id}, im using {user.email}" for user in users]
    return HttpResponse("<br>".join(greetings))

def booking_list(request):
    bookings = Booking.objects.all()
    if not bookings:
        return HttpResponse("No bookings found.")
    greeting = [f"booking ID: {booking.id}, user: {booking.user.username}, Car: {booking.car_id}, Date: {booking.date}" for booking in bookings]
    return HttpResponse("<br>".join(greeting))

def home_view(request):
    return HttpResponse("<h1>Welcome Home<h1>")
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Booking

# Create your views here.

def user_list(request):
    users = User.objects.all()
    if not users:
        return HttpResponse("No Users found.")
    greetings = [f"Hello, {user.email}" for user in users]
    return HttpResponse("<br>".join(greetings))

def booking_list(request):
    bookings = Booking.objects.all()
    if not bookings:
        return HttpResponse("No bookings found.")
    greeting = [f"booking {booking.id}, user: {booking.user_id}, Car: {booking.car_id}" for booking in bookings]
    return HttpResponse("<br>".join(greeting))

def home_view(request):
    return HttpResponse("<h1>Welcome Home<h1>")
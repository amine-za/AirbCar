from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Booking, Partner, Listing
from rest_framework import viewsets
from .serializers import UserSerializer, BookingSerializer, PartnerSerializer, ListingSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

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
    greeting = [f"booking ID: {booking.id}, user: {booking.user.username}, Car: {booking.listing}, Date: {booking.date}" for booking in bookings]
    return HttpResponse("<br>".join(greeting))

def home_view(request):
    return HttpResponse("<h1>Welcome Home<h1>")
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Booking, Partner, Listing
from rest_framework import viewsets, generics, status
from .serializers import UserSerializer, BookingSerializer, PartnerSerializer, ListingSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
import uuid

# Create your views here.

#  This serializer class contains the logic for how to take the incoming 
# data from the request and convert it into a model instance

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

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.email_verification_token = str(uuid.uuid4())  # Generate token for email verification
        user.save()
        # Placeholder for email verification (configured on Day 2)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

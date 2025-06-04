from rest_framework import serializers
from .models import User, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'default_currency', 'is_partner', 'is_verified']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "user_id", "car_id", "date"]
from rest_framework import serializers
from .models import User, Booking, Partner, Listing

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'default_currency', 'is_partner', 'is_verified']

class PartnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Partner
        fields = ['id', 'user', 'company_name', 'tax_id', 'verification_status', 'created_at']

class ListingSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer(read_only=True)
    class Meta:
        model = Listing
        fields = ['id', 'partner', 'make', 'model', 'year', 'price_per_day', 'availability', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    listing = ListingSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ["id", "user", "listing", "date"]
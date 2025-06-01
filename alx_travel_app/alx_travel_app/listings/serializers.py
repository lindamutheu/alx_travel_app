from rest_framework import serializers
from .models import Listing, Booking
from django.contrib.auth import get_user_model


User = get_user_model()

class ListingSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField(read_only=True)  # Or use a nested serializer if needed

    class Meta:
        model = Listing
        fields = [
            'property_id',
            'title',
            'description',
            'location',
            'price_per_night',
            'created_at',
            'updated_at',
        ]
class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    property = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = [
            'booking_id',
            'listing',
            'guest_name'
            'check_in'
            'check_out'
            'created_at',
        ]

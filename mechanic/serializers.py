from rest_framework import serializers
from .models import Service, Booking, Availability, Payment, Review

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)  # Nested service details
    service_id = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), source='service')  # For POSTing service id

    class Meta:
        model = Booking
        fields = ['id', 'customer_name', 'customer_phone', 'customer_email', 'service', 'service_id', 'vehicle_details', 'date', 'time', 'status']


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)  # Nested booking details
    booking_id = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all(), source='booking')  # For POSTing booking id

    class Meta:
        model = Payment
        fields = ['id', 'booking', 'booking_id', 'amount', 'is_paid', 'payment_date']


class ReviewSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)  # Nested booking details
    booking_id = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all(), source='booking')  # For POSTing booking id

    class Meta:
        model = Review
        fields = ['id', 'booking', 'booking_id', 'rating', 'comment', 'date']

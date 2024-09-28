from rest_framework import viewsets
from .models import Service, Booking, Availability, Payment, Review
from .serializers import ServiceSerializer, BookingSerializer, AvailabilitySerializer, PaymentSerializer, ReviewSerializer

# ViewSet for Service
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# ViewSet for Booking
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# ViewSet for Availability
class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

# ViewSet for Payment
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# ViewSet for Review
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

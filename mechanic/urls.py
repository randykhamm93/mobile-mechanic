from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, BookingViewSet, AvailabilityViewSet, PaymentViewSet, ReviewViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'availabilities', AvailabilityViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'reviews', ReviewViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

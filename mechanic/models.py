from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15, null=True, blank=True)
    customer_email = models.EmailField(null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    vehicle_details = models.CharField(max_length=255, null=True, blank=True)  # Store car details
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
    max_length=20, 
    choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed')], 
    default='Pending'
)


    def __str__(self):
        return f"{self.customer_name} - {self.service.name}"


class Availability(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)


class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Rating out of 5
    comment = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

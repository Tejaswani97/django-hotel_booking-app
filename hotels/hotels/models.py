
# hotels/models.py

from django.db import models
from django.contrib.auth.models import User

# Hotel model
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)  # Full hotel address
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.FloatField()
    price_per_night = models.FloatField()
    available_rooms = models.IntegerField()
    destination = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.destination}"

# Booking model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    rooms_booked = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name}"
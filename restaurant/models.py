from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[MaxValueValidator(5)])
    
    def __str__(self) -> str:
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=1, validators=[MaxValueValidator(6)])
    booking_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

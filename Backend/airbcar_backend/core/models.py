from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    default_currency = models.CharField(max_length=3, default='USD')
    is_partner = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} for User {self.user_id}"
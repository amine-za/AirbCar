from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    user_id = models.IntegerField()
    car_id = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} for User {self.user_id}"
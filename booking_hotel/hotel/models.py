from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Room(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Апартаменты №{self.id} - {self.description[:20]}..."


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')

    date_start = models.DateField()
    date_end = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Бронь # {self.id} (Апатаменты №{self.room_id})"

    def clean(self):
        if self.date_start >= self.date_end:
            raise ValidationError('Дата выезда должна быть позже даты заезда')
        if self.date_start < date.today():
            raise ValidationError('Дата заезда не может быть в прошлом')

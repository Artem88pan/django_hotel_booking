from rest_framework import serializers
from booking_hotel.hotel.models import Room, Booking
from django.core.exceptions import ValidationError

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'description', 'price', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'room', 'date_start', 'date_end']

    def validate(self, data):
        if data['date_start'] >= data['date_end']:
            raise serializers.ValidationError({'error': 'Дата выезда должна быть позже даты заезда'})
        return data
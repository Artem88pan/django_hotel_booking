from datetime import date, timedelta
from decimal import Decimal

import pytest
from hotel.models import Booking, Room
from hotel.serializers import BookingSerializer, RoomSerializer
from rest_framework.test import APIClient


# model room test
@pytest.mark.django_db
def test_create_room():
    room = Room.objects.create(
        description="Тестовый номер с балконом",
        price=Decimal("3000.00")
    )

    assert room.id is not None
    assert isinstance(room.description, str)
    assert room.price == Decimal(3000.00)


# model booking test
@pytest.mark.django_db
def test_valid_booking():
    room = Room.objects.create(description="Тестовая", price=1000)
    start = date.today() + timedelta(days=1)
    end = start + timedelta(days=2)
    booking = Booking(room=room, date_start=start, date_end=end)
    booking.full_clean()


@pytest.mark.django_db
def test_valid_booking_dates():
    room = Room.objects.create(description="Тестовая", price=1000)
    date_start = date.today()
    date_end = date_start + timedelta(days=1)

    booking = Booking(room=room, date_start=date_start, date_end=date_end)
    booking.full_clean()
    assert booking.id is None


# serializer test
@pytest.mark.django_db
def test_room_serializer_output():
    room = Room.objects.create(description="Комната", price=500)
    serializer = RoomSerializer(room)
    assert serializer.data["description"] == "Комната"
    assert float(serializer.data["price"]) == 500


@pytest.mark.django_db
def test_booking_serializer_output():
    room = Room.objects.create(description="Комната", price=500)
    booking = Booking.objects.create(
        room=room,
        date_start=date.today() + timedelta(days=1),
        date_end=date.today() + timedelta(days=2)
    )
    serializer = BookingSerializer(booking)
    assert serializer.data["room"] == room.id


# api test room


@pytest.mark.django_db
def test_create_room_api():
    client = APIClient()
    response = client.post("/rooms/", {"description": "API Room", "price": "123.45"}, format="json")
    assert response.status_code == 201
    assert "room_id" in response.data


@pytest.mark.django_db
def test_list_rooms_api():
    Room.objects.create(description="Комната тестовая 1", price=1000)
    Room.objects.create(description="Комната тестовая 2", price=2000)
    client = APIClient()
    response = client.get("/rooms/")
    assert response.status_code == 200
    assert len(response.data) == 2


# api test booking
@pytest.mark.django_db
def test_create_booking_api():
    room = Room.objects.create(description="API бронирование", price=1000)
    client = APIClient()
    response = client.post("/bookings/", {
        "room": room.id,
        "date_start": str(date.today() + timedelta(days=1)),
        "date_end": str(date.today() + timedelta(days=3))
    }, format="json")
    assert response.status_code == 201
    assert "booking_id" in response.data


@pytest.mark.django_db
def test_get_booking_by_room_id():
    room = Room.objects.create(description="Тест бронирования", price=1200)
    Booking.objects.create(
        room=room,
        date_start=date.today() + timedelta(days=1),
        date_end=date.today() + timedelta(days=2)

    )
    client = APIClient()
    response = client.get(f"/bookings/?room_id={room.id}")
    assert response.status_code == 200
    assert len(response.data) == 1

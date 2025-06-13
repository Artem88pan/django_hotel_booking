
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking, Room
from .serializers import BookingSerializer, RoomSerializer


class RoomAPI(APIView):
    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save()
            return Response({"room_id": room.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, room_id):
        try:
            room = Room.objects.get(id=room_id)
            room.delete()
            return Response({"Сообщение": f" Апартамент №{room_id} и все бронирования удалены"},
                             status=status.HTTP_200_OK
                             )
        except Room.DoesNotExist:
            return Response({"error": "номер не найден"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        order_by = request.query_params.get('order_by', 'id')
        order = request.query_params.get('order', 'asc')

        if order_by not in ['price', 'created_at']:
            order_by = 'id'

        if order == 'desc':
            order_by = f'-{order_by}'

        rooms = Room.objects.all().order_by(order_by)

        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


class BookingAPI(APIView):
    def post(self, request):
        try:
            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                booking = serializer.save()
                return Response({"booking_id": booking.id}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id)
            booking.delete()
            return Response({"Сообщение": f"Бронь № {booking_id} удалена"}, status=status.HTTP_200_OK)
        except Booking.DoesNotExist:
            return Response({"error": "бронь не найдена"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        room_id = request.query_params.get('room_id')
        if not room_id:
            return Response({"error": "неверный id"}, status=status.HTTP_400_BAD_REQUEST)

        bookings = Booking.objects.filter(room_id=room_id).order_by("date_start")

        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

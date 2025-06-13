"""URL configuration for booking_hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

Examples
--------
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from hotel.views import BookingAPI, RoomAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/', RoomAPI.as_view(), name='room-list-create'),
    path('rooms/<int:room_id>/', RoomAPI.as_view(), name='room-detail-delete'),
    path('bookings/', BookingAPI.as_view(), name='booking-list-create'),
    path('bookings/<int:booking_id>/', BookingAPI.as_view(), name='booking-detail-delete'),
    path('', lambda request: HttpResponse("Добро пожаловать в систему бронирования!")),
]

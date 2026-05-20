from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('history/', views.booking_history, name='booking_history'),
]

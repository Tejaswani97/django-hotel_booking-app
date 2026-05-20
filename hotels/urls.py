from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),   # ✅ change THIS
    path('book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('logout/', views.logout_view, name='logout'),
]

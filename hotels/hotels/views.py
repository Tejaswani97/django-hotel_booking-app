from django.shortcuts import render
from .models import Hotel

def home(request):
    hotels = Hotel.objects.all()

    # Optional: handle search by destination
    destination = request.GET.get('destination')
    if destination:
        hotels = hotels.filter(destination__icontains=destination)

    context = {
        'hotels': hotels
    }
    return render(request, 'hotels/home.html', context)
# Create your views here.

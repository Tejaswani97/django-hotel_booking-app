from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Booking
from datetime import datetime
from django.contrib.auth import logout
# 🔐 AUTH IMPORTS
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from .forms import RegisterForm
from django.shortcuts import render, redirect

# 🔹 LOGIN VIEW (FIRST PAGE)
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # 👑 ADMIN → ADMIN PANEL
            if user.is_superuser:
                return redirect("/admin/")

            # 👤 USER → HOME PAGE
            return redirect("/home/")

        else:
            return render(request, "hotels/login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "hotels/login.html")


# 🔹 LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('login')  # back to login page


# 🔹 HOME PAGE (SEARCH + BOOKING HISTORY)
def home(request):
    # 🔒 FORCE LOGIN
    if not request.user.is_authenticated:
        return redirect('login')

    query = request.GET.get("q", "")

    # 🔍 SEARCH
    if query:
        hotels = Hotel.objects.filter(name__icontains=query)
    else:
        hotels = Hotel.objects.all()

    # 📌 BOOKING HISTORY
    bookings = Booking.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "hotels/home.html", {
        "hotels": hotels,
        "query": query,
        "bookings": bookings
    })


# 🔹 BOOK HOTEL
def book_hotel(request, hotel_id):
    # 🔒 REQUIRE LOGIN
    if not request.user.is_authenticated:
        return redirect('login')

    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == "POST":
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        rooms = int(request.POST.get("rooms"))

        # 📅 CALCULATE DAYS
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        days = (check_out_date - check_in_date).days

        if days <= 0:
            return render(request, "hotels/book.html", {
                "hotel": hotel,
                "error": "Check-out must be after check-in"
            })

        # 💰 TOTAL PRICE
        total_price = hotel.price_per_night * rooms * days

        # 💾 SAVE BOOKING
        Booking.objects.create(
            user=request.user,
            hotel=hotel,
            check_in=check_in,
            check_out=check_out,
            rooms=rooms,
            total_price=total_price
        )

        # ✅ REDIRECT WITH SUCCESS POPUP
        return redirect("/home/?booked=true")

    return render(request, "hotels/book.html", {"hotel": hotel})
    
def logout_view(request):
    logout(request)
    return redirect('login')  # goes back to login page
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    else:
        form = RegisterForm()

    return render(request, 'hotels/register.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Staff, Items, Testimonial, Booking
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {"items": Items.objects.all(), "teams": Staff.objects.all(), "as": Testimonial.objects.all()}
    return render(request, "index.html", context)


def about(request):
    return render(request, template_name="about.html")


def booking(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        datetime = request.POST.get("datetime")
        no_of_people = request.POST.get("no_of_people")
        special_request = request.POST.get("special_request")
        Booking.objects.create(name=name, email=email, datetime=datetime, no_of_people=no_of_people, special_request=special_request)
        return redirect("booking")
    return render(request, template_name="booking.html")


def menu(request):
    context = {
        "items": Items.objects.all()
    }
    return render(request, "menu.html", context)


def service(request):
    return render(request, template_name="service.html")


def team(request):
    context = {
    "teams": Staff.objects.all(),
    }
    return render(request, "team.html", context)


def testimonial(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        Testimonial.objects.create(name=name, message=message)
        return redirect("testimonial")
    context = {"title": "testimonial", "as": Testimonial.objects.all()}
    return render(request, "testimonial.html", context)


def contact(request):
    return render(request, template_name="contact.html")
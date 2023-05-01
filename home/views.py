from django.shortcuts import render
from .models import Staff
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, template_name="index.html")


def about(request):
    return render(request, template_name="about.html")


def booking(request):
    return render(request, template_name="booking.html")


def menu(request):
    return render(request, template_name="menu.html")


def service(request):
    return render(request, template_name="service.html")


def team(request):
    context = {
    "teams": Staff.objects.all(),
    }
    return render(request, "team.html", context)


def testimonial(request):
    return render(request, template_name="testimonial.html")


def contact(request):
    return render(request, template_name="contact.html")
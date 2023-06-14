from django.shortcuts import render, redirect
from .models import Staff, Items, Testimonial, Booking, Contact
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {"items": Items.objects.all(),
               "teams": Staff.objects.all(),
               "as": Testimonial.objects.all()
               }
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
        Booking.objects.create(name=name, email=email,
                               datetime=datetime,
                               no_of_people=no_of_people,
                               special_request=special_request
                               )
        return redirect("booking")
    return render(request, template_name="booking.html")


@login_required
def staff_page(request):
    context = {"booking_infos": Booking.objects.all(),
               "contacts": Contact.objects.all()
               }
    return render(request, "staff-page.html", context)


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
        Testimonial.objects.create(name=name,
                                   message=message
                                   )
        return redirect("testimonial")
    context = {"title": "testimonial", "as": Testimonial.objects.all()}
    return render(request, "testimonial.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Contact.objects.create(name=name,
                               email=email,
                               subject=subject,
                               message=message
                               )
        return redirect("contact")
    context = {"title": "contact"}
    return render(request, "contact.html", context)


def dining_table(request):
    return render(request, template_name="dining-table.html")


def checkout(request):
    return render(request, template_name="checkout.html")


def delete(request, id):

    try:
        booking = Booking.objects.get(id=id)
    except Booking.DoesNotExist:
        return redirect('staff_page')
    context = {
        "title": "delete", "booking": booking,
    }
    if request.method == "POST":
        Booking.objects.filter(id=id).delete()
        return redirect('staff_page')
    return render(request, "delete.html", context)


def delete_contact(request, id):

    try:
        contact = Contact.objects.get(id=id)
    except Contact.DoesNotExist:
        return redirect('staff_page')
    context = {
        "title": "delete", "contact": contact,
    }
    if request.method == "POST":
        Contact.objects.filter(id=id).delete()
        return redirect('staff_page')
    return render(request, "delete-contact.html", context)
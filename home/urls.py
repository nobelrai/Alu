from django.urls import path
from .views import index, about, booking, menu, service, team, testimonial, contact, staff_page

urlpatterns=[
    path("about/", about, name="about"),
    path("booking/", booking, name="booking"),
    path("menu/", menu, name="menu"),
    path("service/", service, name="service"),
    path("team/", team, name="team"),
    path("contact/", contact, name="contact"),
    path("testimonial/", testimonial, name="testimonial"),
    path("staff-page/", staff_page, name="staff_page"),
    path("", index, name="index"),
]
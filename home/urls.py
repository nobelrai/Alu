from django.urls import path
from .views import index, about, booking, menu, service, team, testimonial, contact

urlpatterns=[
    path("about/", about, name="about"),
    path("booking/", booking, name="booking"),
    path("menu/", menu, name="menu"),
    path("service/", service, name="service"),
    path("team/", team, name="team"),
    path("contact/", contact, name="contact"),
    path("testimonial", testimonial, name="testimonial"),
    path("index/", index, name="index"),
]
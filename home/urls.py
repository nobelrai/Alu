from django.urls import path
from .views import index, about, booking, menu, service, team, testimonial,\
    contact, staff_page, delete, delete_contact
urlpatterns = [
    path("staff-page/", staff_page, name="staff_page"),
    path("about/", about, name="about"),
    path("booking/", booking, name="booking"),
    path("menu/", menu, name="menu"),
    path("service/", service, name="service"),
    path("team/", team, name="team"),
    path("contact/", contact, name="contact"),
    path("testimonial/", testimonial, name="testimonial"),
    path("delete/<int:id>/", delete, name="delete"),
    path("delete-contact/<int:id>/", delete_contact, name="delete_contact"),
    path("", index, name="index"),
]

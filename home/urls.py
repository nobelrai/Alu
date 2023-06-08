from django.urls import path
from .views import index, about, booking, menu, service, team, testimonial,\
    contact, staff_page, dining_table, checkout, delete, delete_contact,login_user

urlpatterns=[
    path("dining-table/", dining_table, name="dining_table"),
    path("staff-page/", staff_page, name="staff_page"),
    path("about/", about, name="about"),
    path("booking/", booking, name="booking"),
    path("menu/", menu, name="menu"),
    path("service/", service, name="service"),
    path("team/", team, name="team"),
    path("contact/", contact, name="contact"),
    path("testimonial/", testimonial, name="testimonial"),
    path("checkout/", checkout, name="checkout"),
    path("delete/<int:id>/", delete, name="delete"),
    path("delete-contact/<int:id>/", delete_contact, name="delete_contact"),
    path('login', login_user, name='login'),
    path("", index, name="index"),
]

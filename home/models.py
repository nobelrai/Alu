from django.db import models
from django.contrib.auth.models import User
# # Create your models here.

GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female')
)


class Staff(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50, null=True)
    designation = models.CharField(max_length=20, null=True)
    facebook = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"


class Items(models.Model):
    name = models.CharField(max_length=20)
    region = models.CharField(max_length=20, null=True)
    price = models.IntegerField()
    description = models.TextField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=12)
    orders = models.ManyToManyField(Items, blank=True)

    def __str__(self):
        return f"{self.name}"


class Testimonial(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    message = models.TextField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"


class Booking(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    no_of_people = models.IntegerField(null=True)
    special_request = models.TextField(max_length=200, null=True)
    pre_order = models.ManyToManyField(Items, blank=True)

    def __str__(self):
        return f"{self.name}"


class Contact(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.name}"

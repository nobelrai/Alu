from django.db import models

# # Create your models here.


class Staff(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
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

    def __str__(self):
        return f"{self.name}"


class Testimonial(models.Model):
    name = models.CharField(max_length=20, null=True)
    message = models.TextField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"


class Booking(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    datetime = models.DateTimeField( auto_now_add=True,null=True)
    no_of_people = models.IntegerField( null=True)
    special_request = models.TextField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"


class nothing(models.Model):
    pass

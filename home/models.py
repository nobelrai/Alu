from django.db import models

# # Create your models here.


class Staff(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

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
    pass


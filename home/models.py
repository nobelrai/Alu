from django.db import models

# # Create your models here.


class Staff(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

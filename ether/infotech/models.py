from django.db import models

# Create your models here.
class form(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=100)
    mobile = models.BigIntegerField()

    def __str__(self) -> str:
        return self.firstname
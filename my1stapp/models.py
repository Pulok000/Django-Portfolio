from django.db import models

# Create your models here.
class student(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name


class contact(models.Model):

    email=models.EmailField(max_length=15)
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.email


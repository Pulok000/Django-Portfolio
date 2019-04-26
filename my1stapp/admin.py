from django.contrib import admin
from .models import student,contact
# Register your models here. #models are basically database structure

admin.site.register(student)
admin.site.register(contact)

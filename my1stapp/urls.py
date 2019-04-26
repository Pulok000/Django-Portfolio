from django.urls import path
from . import views

urlpatterns = [
    path('',views.pokafun, name='home'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('contact',views.Contact, name='contact'),
]
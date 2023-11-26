from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('package/', views.package, name='package'),
    path('destination/', views.destination, name='destination'),
    path('booking/', views.booking, name='booking'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]

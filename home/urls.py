
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/<int:id>/', views.blog_details, name='blog_details'),
    path('services/', views.services, name='services'),
    path('service_booking_apply', views.service_booking_apply, name='service_booking_apply'),
    path('user_comments/', views.user_comments, name='user_comments'),
]
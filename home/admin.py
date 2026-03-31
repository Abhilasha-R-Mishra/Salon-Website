from django.contrib import admin

from .models import ServiceCotegory, ServiceSubCotegory,UserComments,blogs,Booking

# Register your models here.
admin.site.register(ServiceCotegory)
admin.site.register(ServiceSubCotegory)
admin.site.register(UserComments)
admin.site.register(blogs)
admin.site.register(Booking)
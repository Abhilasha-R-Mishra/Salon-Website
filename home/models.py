from datetime import time

from django.db import models

# Create your models here.
from django.db import models

class ServiceCotegory(models.Model):
  serv_cotegory = models.CharField(max_length=500)
  describ_service = models.CharField(max_length=500)

  def __str__(self):
    return self.serv_cotegory


class ServiceSubCotegory(models.Model):
  serv_cotegory = models.ForeignKey(ServiceCotegory, on_delete=models.CASCADE) # This is the foreign key field
  type_of_serv_cotegory = models.CharField(max_length=500)
  about_the_service = models.CharField(max_length=500,default="")
  describ_service = models.CharField(max_length=5000)
  price = models.CharField(max_length=500)
  image = models.ImageField(upload_to='media/')

  # def __str__(self):
  #   return self.type_of_serv_cotegory
  
class UserComments(models.Model):
  user_Name = models.CharField(max_length=255)
  comments = models.CharField(max_length=255)
  u_img = models.ImageField(upload_to='media/', default="")

  def __str__(self):
    return self.user_Name


class blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    headings = models.CharField(max_length=200, default="")
    category = models.ForeignKey(ServiceCotegory, on_delete=models.CASCADE)
    desc1 = models.CharField(max_length=300,default="")
    siub_head1 = models.CharField(max_length=200,default="")
    desc2 = models.CharField(max_length=300,default="")
    sub_head2 = models.CharField(max_length=200,default="")
    desc3 = models.CharField(max_length=300,default="")
    desc4 = models.CharField(max_length=300,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/', default="")

    def __str__(self):
        return self.title
    

class Booking(models.Model):
    user_name = models.CharField(max_length=100, default="")
    service_cotegory = models.CharField(max_length=100, default="")
    selected_service_type = models.CharField(max_length=100, default="")
    email_id = models.CharField(max_length=100, default="")
    mobileNumber = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    booking_date = models.DateField(default=None)
    booking_time = models.TimeField(default=time(10, 0),null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
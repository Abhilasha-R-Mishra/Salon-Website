from datetime import datetime, timezone
import types

from django.shortcuts import redirect, render
import time

from .send_reminder import send_reminder, send_whatsapp_message
from .models import Booking, ServiceCotegory, ServiceSubCotegory, UserComments, blogs
import urllib.parse
from django.core.mail import send_mail
from salons.settings import EMAIL_HOST_USER
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
def home(request):
    service_categories = ServiceCotegory.objects.all()
    service_subcategories = ServiceSubCotegory.objects.all()
    blog_post = blogs.objects.all()
    return render(request, 'home.html', {'service_categories': service_categories, 'service_subcategories': service_subcategories, 'blog_post': blog_post})

def about(request):
    context = {
        "salon_name": "Glow Beauty Salon"
    }
    return render(request, "about.html", context)

def contact(request):
    return render(request, "contact.html")

# gallery,blog, login
def gallery(request):
    service_categories = ServiceCotegory.objects.all()
    service_subcategories = ServiceSubCotegory.objects.all()
    return render(request, "gallery.html", {'service_categories': service_categories, 'service_subcategories': service_subcategories})

def blog(request):
    # Retrieve the specific blog post based on the ID
    blog_post = blogs.objects.all()
    return render(request, "blog.html", {'blog_post': blog_post})

# def blog_details(request, id):
#     # Retrieve the specific blog post based on the ID
#     blog_details = blogs.objects.get(id=id)
#     print("blog_details,", blog_details)
#     return render(request, "blog.html", {'blog_details': blog_details})

def blog_details(request, id):
    blog_details = blogs.objects.get(pk=id)
    return render(request, "blog.html", {"blog_details": blog_details})

def login(request):
    return render(request, "login.html")

def services(request):
    service_subcategories = ServiceSubCotegory.objects.all().order_by('serv_cotegory')
    return render(request, "services.html", {'service_subcategories': service_subcategories})

def service_booking_apply(request):
    if request.method == "POST":
        service_id = request.POST.get("service_id")
        user_name = request.POST.get("user_name")
        email_id = request.POST.get("email_id")
        mobileNumber = request.POST.get("mobileNumber")
        address = request.POST.get("address")
        booking_date = request.POST.get("booking_date")
        booking_time = request.POST.get("booking_time")
        # booking_date = request.POST.get("booking_date")
        service_cotegory=ServiceSubCotegory.objects.get(pk=service_id).serv_cotegory.serv_cotegory,
        selected_service_type=ServiceSubCotegory.objects.get(pk=service_id).type_of_serv_cotegory,
        price=ServiceSubCotegory.objects.get(pk=service_id).price
        print(type(booking_date),booking_date,"=========booking_date=====", booking_time)
    
        booking_data=Booking.objects.create(
            user_name=user_name,
            email_id=email_id,
            mobileNumber=mobileNumber,
            address=address,
            booking_date=booking_date,
            booking_time=booking_time,
            service_cotegory=service_cotegory,
            selected_service_type=selected_service_type,
            price=price

        )
        subject = "Salon Booking Confirmation"
        message = f"""
            Hello {user_name},

            Reminder: Your salon booking is Confirmed 📅

            Service: {selected_service_type}
            Booking Date: {booking_date}
            Booking Time: {booking_time}
            Total Bill: {price}

            See you soon 💇‍♀️
            """
        # send_reminder(user_name, mobileNumber, ServiceSubCotegory.objects.get(pk=service_id).serv_cotegory.serv_cotegory, booking_date)
        recepient = str(email_id)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

        # booking_data=ServiceSubCotegory.objects.filter(pk=service_id)
        # print("service_id", service_id)
        # print("booking_data", booking_data)
        return redirect("services")
    else:
        return redirect('services')



def whatsapp_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # user ka message
        message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

        # simple auto reply
        send_whatsapp_message(sender, "Thank you for contacting our Beauty Parlour 💇‍♀️")

        return JsonResponse({"status": "ok"})
    
from twilio.twiml.messaging_response import MessagingResponse

def whatsapp_reply(request):
    resp = MessagingResponse()
    msg = resp.message("Thanks for contacting us 💅")

    return HttpResponse(str(resp), content_type="text/xml")

def user_comments(request):
    if request.method == "POST":
        user_Name = request.POST.get("user_Name")
        comments = request.POST.get("comments")
        u_img = request.FILES.get("u_img")

        UserComments.objects.create(
            user_Name=user_Name,
            comments=comments,
            u_img=u_img
        )

        return redirect('home')
    else:
        return redirect('home')
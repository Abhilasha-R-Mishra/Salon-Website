from django.core.management.base import BaseCommand
from datetime import date, timedelta

import requests
from .models import Booking
from django.core.mail import send_mail

# class Command(BaseCommand):
def send_reminder(name, phone, service, booking_date):
    help = 'Send booking reminder SMS'

    def handle(self, *args, **kwargs):

        tomorrow = date.today() + timedelta(days=1)

        bookings = Booking.objects.filter(
            booking_date=tomorrow,
            reminder_sent=False
        )

        for booking in bookings:

            message = f"""
        Hello {booking.name},

        Reminder: Your salon booking is tomorrow 📅

        Service: {booking.service}
        Date: {booking.booking_date}

        See you soon 💇‍♀️
            """

            send_sms_via_email(booking.phone, message)

            booking.reminder_sent = True
            booking.save()

        self.stdout.write("Reminders sent successfully ✅")


def send_sms_via_email(phone, message):
    sms_email = f"{phone}@sms.airtel.in"
    send_mail("", message, "your_email@gmail.com", [sms_email])


def send_whatsapp_message(to, message):
    url = "https://graph.facebook.com/v18.0/YOUR_PHONE_NUMBER_ID/messages"

    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }

    requests.post(url, json=payload, headers=headers)
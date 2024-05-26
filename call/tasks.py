from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from core.celery import app

from twilio.rest import Client

@app.task(name='test_email')
def test_call(email):
    subject = f"Test Email from a Schedular"
    
    send_mail(
        subject=subject,
        message="test message",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[
            email,
            # 'branch_email'
        ]
    )

@app.task(name='test_twilio_call')
def test_twilio_call(phone):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    name = 'Alex'
    call = client.calls.create(
        twiml="<Response><Say>Hey Tim, This is a test call from {name}\'s schedular RnD.Alex.</Say></Response>",
        to=f'{phone}',
        from_=settings.TWILIO_FROM_NUMBER,
    )
    
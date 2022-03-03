from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.timezone import  now
from datetime import  timedelta
from users.models import User, EmailVerification
from django.core.mail import send_mail
from django.conf import  settings
from django.utils.timezone import  now
from store.celery import app
import uuid

@app.task
def send_email_verification_tasks(user_id):
    try:
        user = User.objects.get(id=user_id)
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_email_verifivcation()
    except Exception as e:
        print(e)
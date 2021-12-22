from datetime import datetime

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#from stutor.models import subject
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


class tutor_account(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) #one to one, 1 tutor per user, en 1 user per tutor
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    phone_number = PhoneNumberField(null=True, blank =True)
    email = models.EmailField(null=True)
    bank_account = models.CharField(max_length=20, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    #tutor_education_level = models.ForeignKey(to='stutor.education_level', on_delete=models.SET_NULL, null=True)
    #tutor_subject = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True)
    price_an_hour = MoneyField(decimal_places=2, default=0, default_currency='EUR', max_digits=11, null=True)
    profile_picture = models.ImageField(null=True, blank=True, default="defaultprofilepicture.jpeg")

    def __str__(self):
        return self.name


from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

from stutor.models import  subject
from tutor.models import tutor_account


class student_account(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField('student name',max_length= 200, null=True)
    surname = models.CharField(max_length=200, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    phone_number = PhoneNumberField(null=True, blank = True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    student_education_level = models.ForeignKey(to='stutor.education_level', on_delete=models.SET_NULL, null=True)
    student_subject = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True)
    profile_picture = models.ImageField(null=True, blank=True, default="defaultprofilepicture.jpeg")
    linked_tutors = models.ManyToManyField(tutor_account)

    def __str__(self):
        return self.name



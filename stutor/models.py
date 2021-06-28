from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class subject(models.Model):
    subject = models.CharField(max_length=300)

    def __str__(self):
        return self.subject

class education_level(models.Model):
    education_levels = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.education_levels

class student(models.Model):
    name = models.CharField(max_length= 200, null=True)
    surname = models.CharField(max_length=200, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    phone_number = PhoneNumberField(null=True, blank = True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    education_level = models.ForeignKey(education_level, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class tutor(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    phone_number = PhoneNumberField(null=True, blank =True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    education_level = models.ForeignKey(education_level, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class status(models.Model):
    current_status = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.current_status

class session(models.Model):
    date = models.DateTimeField(null=True)
    tutor = models.ForeignKey(tutor, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(student, null=True, on_delete=models.SET_NULL)
    notes = models.FileField(null=True, blank=True)
    current_status = models.ManyToManyField(status)











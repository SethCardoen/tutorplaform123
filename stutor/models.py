from enum import Enum

from django.db import models
from datetime import datetime
from djmoney.models.fields import MoneyField


class LessonFormat(models.Model):
    type = models.CharField(max_length=300)

    def __str__(self):
        return self.type

class LanguageChoice(models.Model):
    language = models.CharField(max_length=300)

    def __str__(self):
        return self.language

class subject(models.Model):
    subject = models.CharField(max_length=300)

    def __str__(self):
        return self.subject

class education_level(models.Model):
    education_levels = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.education_levels

class status(models.Model):
    current_status = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.current_status

class session(models.Model):
    date = models.DateField(default=datetime.now)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    student = models.ForeignKey(to="student.student_account", null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(subject, on_delete=models.SET_NULL, null=True)
    tutor = models.ForeignKey(to="tutor.tutor_account", null=True, on_delete=models.SET_NULL)
    notes = models.FileField(null=True, blank=True, default="No notes")
    description = models.CharField(max_length=300, null=True, blank=True, default="No description")
    price_an_hour = MoneyField(decimal_places=2, default=0, default_currency='EUR', max_digits=11, null=True)
    current_status = models.ForeignKey(status, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subject.subject



'''
# blog/models.py
class BlogContributor(models.Model):
contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
contribution = models.CharField(max_length=255, blank=True)

class Meta:
unique_together = ('contributor', 'blog')
'''










